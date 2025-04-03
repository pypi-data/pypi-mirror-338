import click
import os
import time
import json
import subprocess
import paramiko
from datetime import datetime, timedelta
from dotenv import load_dotenv
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import click_spinner
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
from jdcloud_sdk.services.gcs.client.GcsClient import GcsClient
from jdcloud_sdk.services.gcs.apis.DescribeInstancesRequest import DescribeInstancesRequest
from jdcloud_sdk.services.gcs.apis.DescribeInstanceRequest import DescribeInstanceRequest
from jdcloud_sdk.services.gcs.apis.CreateInstancesRequest import CreateInstancesRequest
from jdcloud_sdk.services.gcs.apis.DeleteInstanceRequest import DeleteInstanceRequest
from jdcloud_sdk.core.logger import Logger
import requests
import uuid

# 导入新版模块
from .main import create_app

logger = Logger(0)


class GCS:
    def __init__(self):
        load_dotenv()
        self.access_key = os.getenv('JD_ACCESS_KEY')
        self.secret_key = os.getenv('JD_SECRET_KEY')
        self.credentials = Credential(self.access_key, self.secret_key)
        self.config = Config(
            scheme=SCHEME_HTTPS,
            timeout=60
        )
        self.client = GcsClient(self.credentials, self.config, logger=logger)
        self.region_id = 'cn-central-xy1'
        self.az = 'cn-central-xy1a'
        

    def create_instance(self, num=1, image_id=None, sku_id=None):
        try:
            # 临时禁用调试输出
            os.environ['JDCLOUD_SDK_DEBUG'] = 'false'
            parameters = {
                'regionId': self.region_id,
                'instanceSpec': {
                    'az': self.az,
                    'count': num,
                    'charge': {
                        "chargeMode": "postpaid_by_duration",
                    },
                    'skuId': sku_id or 'gcssku-dkdueldlsid',
                    'imageId': image_id or 'i-de9b194080374b52a00089b143be',
                }
            }
            request = CreateInstancesRequest(parameters, header={'X-JDCLOUD-PROFILE': 'PROFILE_INNER_CUSTOM'})
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result.get('instanceIds', [])
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None

    def delete_instance(self, instance_id):
        try:
            parameters = {
                'regionId': self.region_id,
                'instanceId': instance_id
            }
            request = DeleteInstanceRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return False
            else:
                return True
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return False

    def list_instances(self):
        try:
            parameters = {
                'regionId': self.region_id,
                'az': self.az,
                'pageNumber': 1,
                'pageSize': 100
            }
            request = DescribeInstancesRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result.get('list', [])
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None

    def get_instance(self, instance_id):
        try:
            parameters = {
                'regionId': self.region_id,
                'instanceId': instance_id
            }
            request = DescribeInstanceRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None


@click.group(cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
def cli():
    """HotPod CLI - A command line tool for managing JD Cloud GCS instances"""
    pass


@cli.command('info', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
def info():
    """Display information about HotPod CLI"""
    click.secho("HotPod CLI", fg='green', bold=True)
    click.secho("A command line tool for managing JD Cloud GCS instances", fg='white')
    click.secho("\nDeveloped by JDCloud AIDC Team", fg='cyan')
    click.secho("Version: 0.1.1", fg='cyan')


@cli.group('instance', cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
def instance():
    """Manage GCS instances"""
    pass


@instance.command('list', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
def instance_list():
    """List all GCS instances"""
    gcs = GCS()
    
    # 加载镜像信息
    current_dir = os.path.dirname(os.path.abspath(__file__))
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
    """Create GCS instances with specified image and SKU"""
    if num < 1 or num > 1:
        click.secho("实例数量只能是1", fg='red')
        return
    
    # 加载镜像和SKU信息
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
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
    """Delete a GCS instance"""
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
    """Show details of a GCS instance"""
    click.secho(f"Retrieving details for instance {id}...", fg='yellow')
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
                click.echo(f"{app_domain}")
            else:
                click.secho("应用: ", fg='cyan', nl=False)
                click.echo("未找到应用信息")
    else:
        click.secho(f"No details found for instance {id}", fg='red')


@click.group('file', cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
def file():
    """文件操作相关命令"""
    pass

cli.add_command(file)

@file.command('upload', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
@click.option('--file', help='本地文件路径，支持相对路径和绝对路径')
@click.option('--dir', help='本地目录路径，支持相对路径和绝对路径')
@click.option('--to', default='/root/netdisk/uploadfiles', help='远程目标目录路径')
@click.option('--instance', required=True, help='目标实例ID')
def file_upload(file, dir, to, instance):
    """上传文件或目录到GCS实例
    
    示例:
    \b
    上传单个文件:
    hotpod file upload --file ./data.txt --instance i-xxx
    
    上传整个目录:
    hotpod file upload --dir ./data_folder --instance i-xxx
    """
    if not file and not dir:
        click.secho("错误: 必须指定 --file 或 --dir 参数", fg='red')
        return
    if file and dir:
        click.secho("错误: --file 和 --dir 参数不能同时使用", fg='red')
        return
        
    # 检查本地路径是否存在
    local_path = file or dir
    if not os.path.exists(local_path):
        click.secho(f"错误: 本地路径 '{local_path}' 不存在", fg='red')
        return
        
    # 获取实例信息以获取SSH连接详情
    gcs = GCS()
    with click_spinner.spinner():
        response = gcs.get_instance(instance)
        
    if not response or 'instance' not in response:
        click.secho(f"错误: 无法获取实例 {instance} 的信息", fg='red')
        return
        
    instance_details = response.get('instance', {})
    ssh_username = instance_details.get('sshUserName')
    ssh_password = instance_details.get('sshPassword')
    ssh_host = instance_details.get('host')
    ssh_port = None
    
    # 查找SSH端口
    ports = instance_details.get('ports', [])
    for port in ports:
        if port.get('appName') == 'SSH':
            ssh_port = port.get('port')
            break
            
    if not all([ssh_username, ssh_password, ssh_host, ssh_port]):
        click.secho("错误: 无法获取完整的SSH连接信息", fg='red')
        return

    # 创建SSH客户端
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # 连接到远程服务器
        click.secho("正在连接到远程服务器...", fg='yellow')
        ssh.connect(
            hostname=ssh_host,
            port=ssh_port,
            username=ssh_username,
            password=ssh_password,
            timeout=30
        )
        
        # 创建SFTP客户端
        sftp = ssh.open_sftp()
        
        try:
            if file:
                # 单文件上传
                _upload_single_file(sftp, file, to)
            else:
                # 目录上传
                _upload_directory(sftp, dir, to)
                
        finally:
            sftp.close()
            
    except paramiko.AuthenticationException:
        click.secho("错误: SSH认证失败，请检查用户名和密码", fg='red')
    except paramiko.SSHException as e:
        click.secho(f"错误: SSH连接错误: {str(e)}", fg='red')
    except Exception as e:
        click.secho(f"上传过程中发生错误: {str(e)}", fg='red')
    finally:
        ssh.close()

def _ensure_remote_dir(sftp, remote_dir):
    """确保远程目录存在，如果不存在则创建"""
    try:
        sftp.stat(remote_dir)
    except FileNotFoundError:
        click.secho(f"创建远程目录: {remote_dir}", fg='yellow')
        current_path = ''
        for dir_name in remote_dir.split('/'):
            if not dir_name:
                continue
            current_path += '/' + dir_name
            try:
                sftp.stat(current_path)
            except FileNotFoundError:
                sftp.mkdir(current_path)

def _upload_single_file(sftp, local_file, remote_dir):
    """上传单个文件到远程目录"""
    _ensure_remote_dir(sftp, remote_dir)
    
    file_name = os.path.basename(local_file)
    remote_file_path = os.path.join(remote_dir, file_name)
    
    click.secho(f"正在上传文件: {file_name}...", fg='yellow')
    with click_spinner.spinner():
        sftp.put(local_file, remote_file_path)
    
    click.secho("文件上传成功！", fg='green')
    click.secho(f"文件位置: {remote_file_path}", fg='cyan')

def _upload_directory(sftp, local_dir, remote_base_dir):
    """递归上传目录及其内容到远程目录"""
    # 获取本地目录的基名
    dir_name = os.path.basename(local_dir.rstrip('/'))
    remote_dir = os.path.join(remote_base_dir, dir_name)
    
    # 确保远程目标目录存在
    _ensure_remote_dir(sftp, remote_dir)
    
    # 统计总文件数
    total_files = sum([len(files) for _, _, files in os.walk(local_dir)])
    uploaded_files = 0
    
    click.secho(f"\n开始上传目录: {dir_name}", fg='yellow')
    click.secho(f"总文件数: {total_files}\n", fg='cyan')
    
    # 递归上传目录内容
    for root, dirs, files in os.walk(local_dir):
        # 计算相对路径
        rel_path = os.path.relpath(root, local_dir)
        if rel_path == '.':
            current_remote_dir = remote_dir
        else:
            current_remote_dir = os.path.join(remote_dir, rel_path)
            _ensure_remote_dir(sftp, current_remote_dir)
        
        # 上传文件
        for file in files:
            local_file = os.path.join(root, file)
            remote_file = os.path.join(current_remote_dir, file)
            
            # 显示进度
            uploaded_files += 1
            progress = (uploaded_files / total_files) * 100
            click.echo(f"\r上传进度: [{uploaded_files}/{total_files}] {progress:.1f}% - {file}", nl=False)
            
            try:
                sftp.put(local_file, remote_file)
            except Exception as e:
                click.secho(f"\n错误: 上传文件 {file} 失败: {str(e)}", fg='red')
                continue
    
    click.echo()  # 换行
    click.secho("\n目录上传完成！", fg='green')
    click.secho(f"目录位置: {remote_dir}", fg='cyan')
    click.secho(f"成功上传 {uploaded_files} 个文件", fg='green')


# 使用新版应用（仅在单独运行cli.py时）
if __name__ == '__main__':
    app = create_app()
    app()
