"""集群相关命令模块"""

import os
import json
import click
import click_spinner
from click_help_colors import HelpColorsGroup, HelpColorsCommand

from ..gcs import GCS

def load_clusters():
    """加载集群配置文件"""
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cluster_file = os.path.join(current_dir, 'data', 'cluster.json')
    
    # 如果文件不存在，创建一个空的配置文件
    if not os.path.exists(cluster_file):
        os.makedirs(os.path.dirname(cluster_file), exist_ok=True)
        with open(cluster_file, 'w', encoding='utf-8') as f:
            json.dump({"clusters": []}, f, ensure_ascii=False, indent=4)
        return {"clusters": []}
    
    try:
        with open(cluster_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        click.secho(f"加载集群配置文件失败: {str(e)}", fg='red')
        return {"clusters": []}

def save_clusters(clusters_data):
    """保存集群配置文件"""
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cluster_file = os.path.join(current_dir, 'data', 'cluster.json')
    
    try:
        with open(cluster_file, 'w', encoding='utf-8') as f:
            json.dump(clusters_data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        click.secho(f"保存集群配置文件失败: {str(e)}", fg='red')
        return False

def create_cluster_group(cli):
    """创建集群命令组
    
    Args:
        cli: CLI主命令组
        
    Returns:
        集群命令组
    """
    @cli.group('cluster', cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
    def cluster():
        """管理实例集群"""
        pass
    
    @cluster.command('create', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--name', required=True, help='集群名称（必须唯一）')
    def create(name):
        """创建新的集群
        
        示例:
        \b
        创建新集群:
        hotpod cluster create --name mycluster
        """
        # 检查集群名称是否为空
        if not name:
            click.secho("错误: 集群名称不能为空", fg='red')
            return
            
        # 加载现有集群
        clusters_data = load_clusters()
        
        # 检查名称是否已存在
        for cluster in clusters_data['clusters']:
            if cluster['name'] == name:
                click.secho(f"错误: 集群名称 '{name}' 已存在", fg='red')
                return
        
        # 创建新集群
        new_cluster = {
            'name': name,
            'instances': []
        }
        
        clusters_data['clusters'].append(new_cluster)
        
        # 保存更新后的配置
        if save_clusters(clusters_data):
            click.secho(f"集群 '{name}' 创建成功!", fg='green')
            click.secho("\n集群信息:", fg='cyan')
            click.echo(f"名称: {name}")
            click.echo(f"实例数量: 0")
        
    @cluster.command('addinstance', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--name', required=True, help='集群名称')
    @click.option('--instance', required=True, multiple=True, help='要添加到集群的实例ID（可指定多个）')
    def addinstance(name, instance):
        """向集群添加实例
        
        示例:
        \b
        添加单个实例:
        hotpod cluster addinstance --name mycluster --instance i-abc123
        
        添加多个实例:
        hotpod cluster addinstance --name mycluster --instance i-abc123 --instance i-def456
        """
        # 检查参数
        if not name:
            click.secho("错误: 集群名称不能为空", fg='red')
            return
            
        if not instance:
            click.secho("错误: 必须指定至少一个实例ID", fg='red')
            return
            
        # 加载集群配置
        clusters_data = load_clusters()
        
        # 查找目标集群
        target_cluster = None
        for cluster in clusters_data['clusters']:
            if cluster['name'] == name:
                target_cluster = cluster
                break
                
        if not target_cluster:
            click.secho(f"错误: 集群 '{name}' 不存在", fg='red')
            return
            
        # 检查实例是否存在
        gcs = GCS()
        invalid_instances = []
        for instance_id in instance:
            with click_spinner.spinner():
                instance_details = gcs.get_instance(instance_id)
                
            if not instance_details:
                invalid_instances.append(instance_id)
                
        if invalid_instances:
            click.secho(f"错误: 以下实例不存在: {', '.join(invalid_instances)}", fg='red')
            return
            
        # 检查实例是否已在集群中
        existing_instances = []
        for instance_id in instance:
            if instance_id in target_cluster['instances']:
                existing_instances.append(instance_id)
                
        if existing_instances:
            click.secho(f"警告: 以下实例已在集群中: {', '.join(existing_instances)}", fg='yellow')
            # 从要添加的实例列表中移除已存在的实例
            instance = [i for i in instance if i not in existing_instances]
            if not instance:
                return
        
        # 添加实例到集群
        target_cluster['instances'].extend(instance)
        
        # 保存更新后的配置
        if save_clusters(clusters_data):
            click.secho(f"成功向集群 '{name}' 添加 {len(instance)} 个实例!", fg='green')
            click.secho("\n添加的实例:", fg='cyan')
            for i, instance_id in enumerate(instance, 1):
                click.echo(f"{i}. {instance_id}")
    
    @cluster.command('list', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    def list_clusters():
        """列出所有集群
        
        示例:
        \b
        列出所有集群:
        hotpod cluster list
        """
        # 加载集群配置
        clusters_data = load_clusters()
        
        if not clusters_data['clusters']:
            click.secho("没有找到任何集群", fg='yellow')
            return
            
        # 显示集群列表
        click.secho(f"\n找到 {len(clusters_data['clusters'])} 个集群:", fg='green')
        click.secho("-" * 50, fg='cyan')
        click.secho(f"{'名称':<20} {'实例数量':<10}", fg='cyan')
        click.secho("-" * 50, fg='cyan')
        
        for cluster in clusters_data['clusters']:
            name = cluster['name']
            instance_count = len(cluster['instances'])
            click.echo(f"{name:<20} {instance_count:<10}")
            
    @cluster.command('show', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--name', required=True, help='要显示详情的集群名称')
    def show(name):
        """显示集群详情
        
        示例:
        \b
        显示集群详情:
        hotpod cluster show --name mycluster
        """
        # 加载集群配置
        clusters_data = load_clusters()
        
        # 查找目标集群
        target_cluster = None
        for cluster in clusters_data['clusters']:
            if cluster['name'] == name:
                target_cluster = cluster
                break
                
        if not target_cluster:
            click.secho(f"错误: 集群 '{name}' 不存在", fg='red')
            return
            
        # 显示集群详情
        click.secho("\n集群详情:", fg='green')
        click.echo(f"名称: {name}")
        click.echo(f"实例数量: {len(target_cluster['instances'])}")
        gcs = GCS()
        if target_cluster['instances']:
            click.secho("\n实例列表:", fg='cyan')
            for i, instance_id in enumerate(target_cluster['instances'], 1):
                instance_details = gcs.get_instance(instance_id)
                if instance_details:
                    click.echo(f"{i}. {instance_id}")
                else:
                    click.secho(f"{i}. '{instance_id}' 已被删除", fg='red')
                
    @cluster.command('removeinstance', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--name', required=True, help='集群名称')
    @click.option('--instance', required=True, multiple=True, help='要从集群中移除的实例ID（可指定多个）')
    def removeinstance(name, instance):
        """从集群中移除实例
        
        示例:
        \b
        移除单个实例:
        hotpod cluster removeinstance --name mycluster --instance i-abc123
        
        移除多个实例:
        hotpod cluster removeinstance --name mycluster --instance i-abc123 --instance i-def456
        """
        # 检查参数
        if not name:
            click.secho("错误: 集群名称不能为空", fg='red')
            return
            
        if not instance:
            click.secho("错误: 必须指定至少一个实例ID", fg='red')
            return
            
        # 加载集群配置
        clusters_data = load_clusters()
        
        # 查找目标集群
        target_cluster = None
        for cluster in clusters_data['clusters']:
            if cluster['name'] == name:
                target_cluster = cluster
                break
                
        if not target_cluster:
            click.secho(f"错误: 集群 '{name}' 不存在", fg='red')
            return
            
        # 检查实例是否在集群中
        not_found_instances = []
        for instance_id in instance:
            if instance_id not in target_cluster['instances']:
                not_found_instances.append(instance_id)
                
        if not_found_instances:
            click.secho(f"错误: 以下实例不在集群中: {', '.join(not_found_instances)}", fg='red')
            return
            
        # 从集群中移除实例
        for instance_id in instance:
            target_cluster['instances'].remove(instance_id)
            
        # 保存更新后的配置
        if save_clusters(clusters_data):
            click.secho(f"成功从集群 '{name}' 移除 {len(instance)} 个实例!", fg='green')
            click.secho("\n移除的实例:", fg='cyan')
            for i, instance_id in enumerate(instance, 1):
                click.echo(f"{i}. {instance_id}")
                
    @cluster.command('delete', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--name', required=True, help='要删除的集群名称')
    def delete(name):
        """删除集群
        
        示例:
        \b
        删除集群:
        hotpod cluster delete --name mycluster
        """
        # 检查参数
        if not name:
            click.secho("错误: 集群名称不能为空", fg='red')
            return
            
        # 加载集群配置
        clusters_data = load_clusters()
        
        # 查找并删除目标集群
        found = False
        for i, cluster in enumerate(clusters_data['clusters']):
            if cluster['name'] == name:
                del clusters_data['clusters'][i]
                found = True
                break
                
        if not found:
            click.secho(f"错误: 集群 '{name}' 不存在", fg='red')
            return
            
        # 保存更新后的配置
        if save_clusters(clusters_data):
            click.secho(f"集群 '{name}' 删除成功!", fg='green')
    
    return cluster

# 用于直接在main.py中创建命令组的函数
def create_cluster_group_main(cli):
    """创建集群命令组供main.py使用"""
    return create_cluster_group(cli) 