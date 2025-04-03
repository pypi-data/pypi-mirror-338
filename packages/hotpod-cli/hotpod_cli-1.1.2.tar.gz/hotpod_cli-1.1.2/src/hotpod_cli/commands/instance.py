"""实例相关命令模块"""

import os
import json
import click
import click_spinner
from datetime import datetime, timedelta
from click_help_colors import HelpColorsGroup, HelpColorsCommand

from ..gcs import GCS


def create_instance_group(cli):
    """创建实例命令组
    
    Args:
        cli: CLI主命令组
        
    Returns:
        实例命令组
    """
    @cli.group('instance', cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
    def instance():
        """管理GCS实例"""
        pass
    
    @instance.command('list', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    def instance_list():
        """列出所有GCS实例"""
        gcs = GCS()
        
        # 加载镜像信息
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            with open(os.path.join(current_dir, 'image.json'), 'r', encoding='utf-8') as f:
                images = json.load(f)
                # 创建imageId到name的映射
                image_map = {image['imageId']: image['name'] for image in images}
        except Exception as e:
            click.secho(f"Warning: 无法加载镜像信息: {str(e)}", fg='yellow')
            image_map = {}
        
        with click_spinner.spinner():
            instances = gcs.list_instances()

        if instances is not None:
            if len(instances) == 0:
                click.secho("No instances found", fg='yellow')
            else:
                # 计算状态统计
                running_count = sum(1 for instance in instances if instance.get('status') == 'running')
                stopped_count = sum(1 for instance in instances if instance.get('status') == 'stopped')
                
                # 输出状态统计
                click.secho("\nInstance Status Summary:", fg='green', bold=True)
                click.secho(f"Running: {running_count}", fg='cyan')
                click.secho(f"Stopped: {stopped_count}", fg='yellow')
                click.secho(f"Total: {len(instances)}\n", fg='white')

                # 定义列宽
                id_width = 40
                name_width = 20
                app_width = 30  # 新增App列宽度
                status_width = 10
                time_width = 20

                click.secho("GCS Instances:", fg='green', bold=True)
                
                # 修改表头格式，添加App列
                header = f"{'ID':<{id_width}} {'Name':<{name_width}} {'App':<{app_width}} {'Status':<{status_width}} {'Creation Time (UTC+8)'}"
                click.secho(header, fg='cyan')
                click.secho("-" * (id_width + name_width + app_width + status_width + time_width), fg='cyan')
                
                for instance in instances:
                    instance_id = instance.get('instanceId', 'N/A')
                    instance_name = instance.get('instanceName', 'N/A')
                    image_id = instance.get('imageId', 'N/A')
                    app_name = image_map.get(image_id, 'Unknown')  # 获取镜像名称
                    status = instance.get('status', 'N/A')
                    created_time = instance.get('charge', {}).get('chargeStartTime', 'N/A')
                    
                    # 转换时间为北京时间
                    if created_time != 'N/A':
                        created_time = created_time.replace('Z', '').split('.')[0]
                        utc_time = datetime.strptime(created_time, '%Y-%m-%dT%H:%M:%S')
                        beijing_time = utc_time + timedelta(hours=8)
                        created_time = beijing_time.strftime('%Y-%m-%d %H:%M:%S')
                    
                    # 根据状态使用不同的颜色
                    status_color = 'green' if status == 'running' else 'yellow'
                    colored_status = click.style(f"{status:<{status_width}}", fg=status_color)
                    
                    # 计算中文字符的额外宽度（对于name和app_name）
                    name_extra_width = sum(1 for c in instance_name if ord(c) > 127)
                    name_padding = name_width - name_extra_width
                    
                    app_extra_width = sum(1 for c in app_name if ord(c) > 127)
                    app_padding = app_width - app_extra_width
                    
                    # 构建输出行
                    line = (
                        f"{instance_id:<{id_width}}"
                        f"{instance_name:<{name_padding}}"
                        f"{app_name:<{app_padding}}"
                        f"{colored_status}"
                        f"{created_time}"
                    )
                    click.echo(line)
    
    @instance.command('create', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--imageid', help='ID of the image to use for the instance')
    @click.option('--sku', help='ID of the SKU to use for the instance')
    @click.option('--num', default=1, help='Number of instances to create', type=int)
    def instance_create(imageid, sku, num):
        """创建GCS实例，指定镜像和SKU"""
        if num < 1 or num > 1:
            click.secho("实例数量只能是1", fg='red')
            return
        
        # 加载镜像和SKU信息
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        try:
            with open(os.path.join(current_dir, 'image.json'), 'r', encoding='utf-8') as f:
                images = json.load(f)
        except Exception as e:
            click.secho(f"Error loading image information: {str(e)}", fg='red')
            return
            
        try:
            with open(os.path.join(current_dir, 'sku.json'), 'r', encoding='utf-8') as f:
                skus = json.load(f)
        except Exception as e:
            click.secho(f"Error loading SKU information: {str(e)}", fg='red')
            return
        
        # 如果未指定镜像ID，让用户选择镜像
        if not imageid:
            click.secho("\n请选择要使用的镜像:", fg='green', bold=True)
            for idx, image in enumerate(images):
                click.secho(f"[{idx+1}] {image['name']}", fg='cyan')
                click.echo(f"    描述: {image['description']}")
                click.echo(f"    ID: {image['imageId']}")
                
            while True:
                choice = click.prompt("请输入镜像编号", type=int)
                if 1 <= choice <= len(images):
                    imageid = images[choice-1]['imageId']
                    click.secho(f"已选择镜像: {images[choice-1]['name']}", fg='green')
                    break
                else:
                    click.secho("无效的选择，请重新输入", fg='red')
        
        # 如果未指定SKU ID，让用户选择SKU
        if not sku:
            click.secho("\n请选择要使用的SKU:", fg='green', bold=True)
            for idx, sku_info in enumerate(skus):
                click.secho(f"[{idx+1}] {sku_info['name']}", fg='cyan')
                click.echo(f"    ID: {sku_info['skuId']}")
                
            while True:
                choice = click.prompt("请输入SKU编号", type=int)
                if 1 <= choice <= len(skus):
                    sku = skus[choice-1]['skuId']
                    click.secho(f"已选择SKU: {skus[choice-1]['name']}", fg='green')
                    break
                else:
                    click.secho("无效的选择，请重新输入", fg='red')
        
        click.secho(f"\n创建 {num} 个GCS实例...", fg='yellow')
        gcs = GCS()
        with click_spinner.spinner():
            instance_ids = gcs.create_instance(num, imageid, sku)

        if instance_ids:
            click.secho("\n成功创建实例:", fg='green')
            for idx, instance_id in enumerate(instance_ids):
                click.secho(f"实例 {idx+1}: {instance_id}", fg='cyan')
        else:
            click.secho("创建实例失败", fg='red')
    
    @instance.command('delete', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--id', required=True, help='ID of the instance to delete')
    def instance_delete(id):
        """删除GCS实例"""
        click.secho(f"Deleting instance {id}...", fg='yellow')
        gcs = GCS()
        with click_spinner.spinner():
            success = gcs.delete_instance(id)

        if success:
            click.secho(f"Successfully deleted instance {id}", fg='green')
        else:
            click.secho(f"Failed to delete instance {id}", fg='red')
    
    @instance.command('show', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--id', required=True, help='ID of the instance to show details for')
    def instance_show(id):
        """显示GCS实例详情"""
        # click.secho(f"Retrieving details for instance {id}...", fg='yellow')
        gcs = GCS()
        with click_spinner.spinner():
            response = gcs.get_instance(id)

        if response and 'instance' in response:
            # 获取真正的实例信息，在instance键下
            instance_details = response.get('instance', {})
            
            click.secho("\nInstance Details:", fg='green', bold=True)
            
            # 基本信息 - 调整输出格式: 键和值在同一行
            click.secho("ID: ", fg='cyan', nl=False)
            click.echo(instance_details.get('instanceId', 'N/A'))
            
            click.secho("Name: ", fg='cyan', nl=False)
            click.echo(instance_details.get('instanceName', 'N/A'))
            
            # 创建时间（转换为北京时间）
            created_time = instance_details.get('charge', {}).get('chargeStartTime', 'N/A')
            if created_time != 'N/A':
                created_time = created_time.replace('Z', '').split('.')[0]
                utc_time = datetime.strptime(created_time, '%Y-%m-%dT%H:%M:%S')
                beijing_time = utc_time + timedelta(hours=8)
                created_time = beijing_time.strftime('%Y-%m-%d %H:%M:%S')
            click.secho("创建时间: ", fg='cyan', nl=False)
            click.echo(created_time)
            
            # 计费类型
            charge_mode = instance_details.get('charge', {}).get('chargeMode', 'N/A')
            if charge_mode == 'postpaid_by_duration':
                charge_mode = '按配置'
            elif charge_mode == 'prepaid_by_duration':
                charge_mode = '包年包月'
            click.secho("计费类型: ", fg='cyan', nl=False)
            click.echo(charge_mode)
            
            # SSH信息
            ssh_username = instance_details.get('sshUserName', 'N/A')
            ssh_password = instance_details.get('sshPassword', 'N/A')
            ssh_host = instance_details.get('host', 'N/A')
            ssh_port = None
            
            # 查找SSH端口
            ports = instance_details.get('ports', [])
            for port in ports:
                if port.get('appName') == 'SSH':
                    ssh_port = port.get('port')
                    break
                    
            click.secho("SSH信息:", fg='cyan')
            if ssh_username != 'N/A' and ssh_host != 'N/A' and ssh_port:
                click.echo(f"  访问链接: ssh {ssh_username}@{ssh_host} -p {ssh_port}")
                click.echo(f"  密码: {ssh_password}")
            else:
                click.echo(f"  访问链接: ssh {ssh_username if ssh_username != 'N/A' else '用户名'}@{ssh_host} -p {ssh_port if ssh_port else '端口'}")
                click.echo(f"  密码: {ssh_password}")
                
            # JupyterLab信息
            jupyter_token = instance_details.get('jupyter', 'N/A')
            jupyter_endpoint = None
            
            # 查找JupyterLab endpoint
            cluster_ip_ports = instance_details.get('clusterIpPorts', [])
            for app in cluster_ip_ports:
                if app.get('appName') == 'JupyterLab':
                    jupyter_endpoint = app.get('appDomain')
                    break
                    
            click.secho("JupyterLab: ", fg='cyan', nl=False)
            if jupyter_endpoint and jupyter_token != 'N/A':
                click.echo(f"http://{jupyter_endpoint}/lab?token={jupyter_token}")
            else:
                click.echo("信息不完整")
                
            # 应用信息 - 根据PRD新增
            app_domain = None
            for port in ports:
                if port.get('targetPort') == 27777:
                    app_domain = port.get('appDomain')
                    app_name = port.get('appName', '未命名应用')
                    break
                    
            if app_domain:
                click.secho(f"应用({app_name}): ", fg='cyan', nl=False)
                click.echo(f"{app_domain}")
            else:
                # 尝试从clusterIpPorts查找targetPort为27777的应用
                for port in cluster_ip_ports:
                    if port.get('targetPort') == 27777:
                        app_domain = port.get('appDomain')
                        app_name = port.get('appName', '未命名应用')
                        break
                        
                if app_domain:
                    click.secho(f"应用({app_name}): ", fg='cyan', nl=False)
                    click.echo(f"http://{app_domain}")
                else:
                    click.secho("应用: ", fg='cyan', nl=False)
                    click.echo("未找到应用信息")
        else:
            click.secho(f"No details found for instance {id}", fg='red')
        
    return instance 