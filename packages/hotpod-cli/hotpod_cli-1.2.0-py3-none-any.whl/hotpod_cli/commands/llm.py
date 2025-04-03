"""LLM相关命令模块"""

import os
import json
import time
import click
import random
import requests
import click_spinner
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from litellm import completion, acompletion
import asyncio

from ..gcs import GCS

def load_clusters():
    """加载集群配置文件"""
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cluster_file = os.path.join(current_dir, 'data', 'cluster.json')
    
    try:
        with open(cluster_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        click.secho(f"加载集群配置文件失败: {str(e)}", fg='red')
        return {"clusters": []}

def get_cluster_instance(cluster_name):
    """从指定集群中随机选择一个实例
    
    Args:
        cluster_name (str): 集群名称
        
    Returns:
        str: 实例ID
        
    Raises:
        click.ClickException: 当集群不存在或没有可用实例时
    """
    clusters_data = load_clusters()
    
    # 查找目标集群
    target_cluster = None
    for cluster in clusters_data['clusters']:
        if cluster['name'] == cluster_name:
            target_cluster = cluster
            break
            
    if not target_cluster:
        raise click.ClickException(f"错误: 集群 '{cluster_name}' 不存在")
        
    # 检查集群是否有实例
    if not target_cluster['instances']:
        raise click.ClickException(f"错误: 集群 '{cluster_name}' 中没有实例")
        
    # 随机选择一个实例
    return random.choice(target_cluster['instances'])

def create_llm_group(cli):
    """创建LLM命令组
    
    Args:
        cli: CLI主命令组
        
    Returns:
        LLM命令组
    """
    @cli.group('llm', cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
    def llm():
        """管理大语言模型任务"""
        pass
    
    @llm.command('runtask', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--instance', help='GCS实例ID，如不指定则自动创建')
    @click.option('--cluster', help='集群名称，如果指定则从集群中随机选择实例')
    @click.option('--model', default='qwq', help='大语言模型类型 (deepseek 或 qwq)')
    @click.option('--prompt', help='发送给模型的提示词')
    @click.option('--debug', is_flag=True, help='启用调试模式')
    def llm_runtask(instance, cluster, model, prompt, debug):
        """运行大语言模型任务
        
        示例:
        \b
        向特定实例的模型发送提示词:
        hotpod llm runtask --instance i-xxx --model deepseek --prompt "你好，请介绍一下自己"
        
        使用指定集群中的实例运行任务:
        hotpod llm runtask --cluster yunding --model qwq --prompt "你好"
        
        自动创建实例并运行任务:
        hotpod llm runtask --model qwq --prompt "请用python实现一个快速排序算法"
        """
        # 检查参数冲突
        if instance and cluster:
            click.secho("错误: 不能同时指定 --instance 和 --cluster", fg='red')
            return
            
        if debug:
            click.secho("\n命令参数:", fg='cyan')
            click.echo(f"instance: {instance}")
            click.echo(f"cluster: {cluster}")
            click.echo(f"model: {model}")
            click.echo(f"prompt: {prompt}")
            click.echo(f"debug: {debug}")
            
        # 检查模型参数有效性
        valid_models = ['deepseek', 'qwq']
        if model not in valid_models:
            click.secho(f"错误: 不支持的模型类型 '{model}'，可用选项: {', '.join(valid_models)}", fg='red')
            return
            
        # 模型对应的镜像ID
        model_image_map = {
            'deepseek': 'i-06a91577a5814a42be4bfd22aa57',
            'qwq': 'i-de9b194080374b52a00089b143be'
        }
        
        # 获取所需的镜像ID
        required_image_id = model_image_map[model]
        
        # 初始化GCS客户端
        gcs = GCS()
        instance_created = False
        instance_details = None
        
        # 如果指定了集群，从集群中选择实例
        if cluster:
            instance = get_cluster_instance(cluster)
            if debug:
                click.secho(f"从集群 '{cluster}' 中选择实例: {instance}", fg='green')
        
        # 如果未指定实例和集群，创建新实例
        if not instance:
            click.secho(f"未指定实例ID，将创建新的{model}实例...", fg='yellow')
            
            # 为qwq模型使用指定的SKU
            sku_id = 'gcssku-dkdueldlsid'
            
            # 创建实例
            click.secho(f"正在创建{model}实例...", fg='yellow')
            with click_spinner.spinner():
                instance_ids = gcs.create_instance(1, required_image_id, sku_id)
                
            if not instance_ids:
                click.secho("创建实例失败", fg='red')
                return
                
            instance = instance_ids[0]
            instance_created = True
            click.secho(f"成功创建实例: {instance}", fg='green')
            
            # 获取实例详情
            click.secho(f"获取实例详情...", fg='yellow')
            max_attempts = 30
            for attempt in range(max_attempts):
                with click_spinner.spinner():
                    response = gcs.get_instance(instance)
                    
                if not response or 'instance' not in response:
                    time.sleep(5)
                    continue
                    
                instance_details = response.get('instance', {})
                status = instance_details.get('status')
                click.secho(f"实例状态: {status}...", fg='yellow')
                
                if status == 'running':
                    break
                
                time.sleep(10)
                
            if not instance_details or instance_details.get('status') != 'running':
                click.secho(f"实例未能在规定时间内启动", fg='red')
                return
        else:
            # 如果指定了实例，检查它的镜像是否与所需模型匹配
            with click_spinner.spinner():
                response = gcs.get_instance(instance)
                
            if not response or 'instance' not in response:
                click.secho(f"无法获取实例 {instance} 的详细信息", fg='red')
                return
                
            instance_details = response.get('instance', {})
            instance_image_id = instance_details.get('imageId', '')
            model_name = None
            
            for m_name, image_id in model_image_map.items():
                if instance_image_id == image_id:
                    model_name = m_name
                    break
            
            if model_name and model_name != model:
                click.secho(f"警告: 指定实例的模型类型为 {model_name}，而不是请求的 {model}", fg='yellow')
                model = model_name
        
        # 查找模型API端点和UI端点
        model_url = None
        model_ui_url = None
        cluster_ip_ports = instance_details.get('clusterIpPorts', [])
        
        for port_info in cluster_ip_ports:
            if port_info.get('targetPort') == 27777:
                model_ui_url = port_info.get('appDomain', '')
                tempurl_list = model_ui_url.split('.')
                model_url = f'http://{tempurl_list[0]}-api.' + '.'.join(tempurl_list[1:])
                break
                
        if not model_url:
            click.secho("无法找到模型API端点", fg='red')
            return
            
        click.secho(f"模型API地址: {model_url}", fg='green')
        click.secho(f"模型UI地址: {model_ui_url}", fg='green')
            
        if not prompt:
            click.secho("未提供提示词，仅显示模型访问地址", fg='yellow')
            return 
        else:
            click.secho(f"向模型 {model} 发送提示词...", fg='yellow')
            try:
                response = completion(
                    model=f"ollama_chat/{model}", 
                    messages=[{ "content": prompt ,"role": "user"}], 
                    api_base=model_url,
                    stream=True
                )
                for chunk in response:
                    print(chunk['choices'][0]['delta'].get('content', ''), end='', flush=True)
                print()  # 添加最后的换行
            except Exception as e:
                click.secho(f"请求模型API失败: {str(e)}", fg='red')
                
        # 提示实例创建信息
        if instance_created:
            click.secho("\n注意：该实例为自动创建，任务完成后不会被删除", fg='yellow')
            click.secho("如需删除该实例，请使用命令:", fg='yellow')
            click.echo(f"hotpod instance delete --id {instance}")
                
    return llm