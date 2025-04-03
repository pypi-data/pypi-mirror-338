"""ComfyUI相关命令模块"""

import os
import json
import uuid
import time
import click
import random
import requests
import paramiko
import click_spinner
from urllib.parse import urlparse
from click_help_colors import HelpColorsGroup, HelpColorsCommand

from ..gcs import GCS
from ..utils.ssh import get_ssh_connection, upload_single_file, ensure_remote_dir
from ..utils.click_utils import DynamicCommand

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

class ComfyUITask:
    """ComfyUI任务处理类"""
    def __init__(self, task_file_or_name, instance_id=None, cluster_name=None, debug=False):
        """初始化任务处理类
        
        Args:
            task_file_or_name (str): 任务文件路径或任务名称
            instance_id (str, optional): GCS实例ID
            cluster_name (str, optional): 集群名称
            debug (bool, optional): 是否启用调试模式
        """
        self.debug = debug
        self.gcs = GCS()
        self.task_config = None
        self.workflow_data = None
        self.instance_details = None
        self.instance_created = False
        self.output_node_id = None
        self.output_filename_prefix = None
        self.uploaded_files = {}
        self.user_params = {}
        self.instance_id = instance_id
        self.cluster_name = cluster_name
        self.task_file = None
        
        # 如果指定了集群名称，从集群中选择实例
        if cluster_name:
            self.instance_id = get_cluster_instance(cluster_name)
            click.secho(f"从集群 '{cluster_name}' 中选择实例: {self.instance_id}", fg='green')
        
        # 判断是否是任务名称而不是完整路径
        if os.path.exists(task_file_or_name):
            # 如果是直接存在的文件路径，直接使用
            self.task_file = task_file_or_name
            if self.debug:
                click.secho(f"使用指定的任务文件路径: {task_file_or_name}", fg='cyan')
        else:
            # 如果文件不存在，尝试解析为任务名称
            # 获取tasks目录的路径
            current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            tasks_dir = os.path.join(current_dir, 'tasks')
            
            # 先尝试直接拼接任务名称
            task_file = os.path.join(tasks_dir, f"{task_file_or_name}.json")
            
            if self.debug:
                click.secho(f"尝试查找任务文件: {task_file}", fg='cyan')
                click.secho(f"任务目录内容: {os.listdir(tasks_dir)}", fg='cyan')
                
            if os.path.exists(task_file):
                self.task_file = task_file
                if self.debug:
                    click.secho(f"找到任务文件: {task_file}", fg='green')
            else:
                # 如果没有找到，检查是否为不带.json后缀的完整路径
                alt_file = f"{task_file_or_name}.json" if not task_file_or_name.endswith('.json') else task_file_or_name
                if os.path.exists(alt_file):
                    self.task_file = alt_file
                    if self.debug:
                        click.secho(f"找到备选任务文件: {alt_file}", fg='green')
                else:
                    # 列出可用的任务文件
                    available_tasks = [os.path.splitext(f)[0] for f in os.listdir(tasks_dir) if f.endswith('.json')]
                    task_list = ", ".join(available_tasks)
                    click.secho(f"错误: 任务 '{task_file_or_name}' 不存在", fg='red')
                    click.secho(f"可用的任务: {task_list}", fg='yellow')

    def load_task_config(self):
        """加载任务配置"""
        if not self.task_file:
            click.secho("任务文件未指定或不存在", fg='red')
            return False
            
        try:
            with open(self.task_file, 'r', encoding='utf-8') as f:
                self.task_config = json.load(f)
                self.workflow_data = self.task_config.get('prompt_template', {}).copy()
                if self.debug:
                    click.secho("\n任务配置:", fg='cyan')
                    click.echo(json.dumps(self.task_config, ensure_ascii=False, indent=2))
            return True
        except Exception as e:
            click.secho(f"加载任务配置失败: {str(e)}", fg='red')
            return False

    def ensure_instance(self):
        """确保实例可用，如果需要则创建新实例"""
        if not self.instance_id:
            if not self.create_instance():
                return False
        
        # 获取实例详情并确保实例运行
        response = self.gcs.get_instance(self.instance_id)
        if not response or 'instance' not in response:
            click.secho(f"无法获取实例 {self.instance_id} 的详细信息", fg='red')
            return False
        
        self.instance_details = response.get('instance', {})
        return self._ensure_instance_running()

    def create_instance(self):
        """创建新的ComfyUI实例"""
        click.secho("未指定实例，正在创建新实例...", fg='yellow')
        
        # 加载镜像信息
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            with open(os.path.join(current_dir, 'image.json'), 'r', encoding='utf-8') as f:
                images = json.load(f)
                # 查找ComfyUI镜像
                comfyui_image = next((image for image in images if 'comfyui' in image['name'].lower()), None)
                if not comfyui_image:
                    click.secho("无法找到ComfyUI镜像", fg='red')
                    return False
                imageid = comfyui_image['imageId']
        except Exception as e:
            click.secho(f"加载镜像信息失败: {str(e)}", fg='red')
            return False
        
        # 加载SKU信息
        try:
            with open(os.path.join(current_dir, 'sku.json'), 'r', encoding='utf-8') as f:
                skus = json.load(f)
                # 获取第一个SKU
                sku = skus[0]['skuId']
        except Exception as e:
            click.secho(f"加载SKU信息失败: {str(e)}", fg='red')
            return False
        
        # 创建实例
        click.secho(f"正在创建ComfyUI实例，使用镜像: {comfyui_image['name']}...", fg='yellow')
        with click_spinner.spinner():
            instance_ids = self.gcs.create_instance(1, imageid, sku)
            
        if not instance_ids:
            click.secho("创建实例失败", fg='red')
            return False
            
        self.instance_id = instance_ids[0]
        self.instance_created = True
        click.secho(f"成功创建实例: {self.instance_id}", fg='green')
        return True

    def _ensure_instance_running(self):
        """确保实例处于运行状态"""
        status = self.instance_details.get('status')
        if status != 'running':
            if self.instance_created:
                click.secho(f"等待实例启动，当前状态: {status}...", fg='yellow')
                
                # 等待实例启动
                max_attempts = 30
                for attempt in range(max_attempts):
                    with click_spinner.spinner():
                        time.sleep(10)  # 等待10秒
                        response = self.gcs.get_instance(self.instance_id)
                        
                    if not response or 'instance' not in response:
                        continue
                        
                    self.instance_details = response.get('instance', {})
                    status = self.instance_details.get('status')
                    click.secho(f"实例状态: {status}...", fg='yellow')
                    
                    if status == 'running':
                        break
                        
                if status != 'running':
                    click.secho(f"实例未能在规定时间内启动，当前状态: {status}", fg='red')
                    return False
            else:
                click.secho(f"实例 {self.instance_id} 未运行。当前状态: {status}", fg='red')
                return False
        return True

    def process_workflow(self):
        """处理工作流配置，包括生成UUID等"""
        # 处理输出节点配置
        if 'config' in self.task_config and 'outputs' in self.task_config['config']:
            for output_config in self.task_config['config']['outputs']:
                if self._should_generate_uuid(output_config):
                    node_id = str(output_config['node_id'])
                    self.output_node_id = node_id
                    filename_key = output_config['replace'].get('key', 'filename_prefix')
                    self._update_node_uuid(node_id, output_config)
                    # 保存生成的文件名前缀用于后续输出URL生成
                    if node_id in self.workflow_data and 'inputs' in self.workflow_data[node_id]:
                        self.output_filename_prefix = self.workflow_data[node_id]['inputs'].get(filename_key)

        # 如果未找到配置的输出节点，尝试自动找出SaveImage节点
        if not self.output_node_id:
            for node_id, node_data in self.workflow_data.items():
                if node_data.get('class_type') == 'SaveImage':
                    self.output_node_id = node_id
                    if 'inputs' in node_data and 'filename_prefix' in node_data['inputs']:
                        # 为找到的SaveImage节点生成UUID
                        new_uuid = str(uuid.uuid4())
                        node_data['inputs']['filename_prefix'] = new_uuid
                        self.output_filename_prefix = new_uuid
                        if self.debug:
                            click.secho(f"自动为SaveImage节点 {node_id} 生成UUID: {new_uuid}", fg='green')
                    break

        # 处理输入配置
        if 'config' in self.task_config and 'inputs' in self.task_config['config']:
            self._process_input_configs()

        if self.debug:
            self._print_debug_info()

    def _should_generate_uuid(self, config):
        """检查是否需要为配置生成UUID"""
        return ('replace' in config and 
                config['replace'].get('value') == 'HOTPOD_UUID')

    def _update_node_uuid(self, node_id, config):
        """更新节点的UUID"""
        if (node_id in self.workflow_data and 
            'inputs' in self.workflow_data[node_id]):
            new_uuid = str(uuid.uuid4())
            key = config['replace'].get('key', 'filename_prefix')
            self.workflow_data[node_id]['inputs'][key] = new_uuid
            if self.debug:
                click.secho(f"为节点 {node_id} 生成UUID: {new_uuid}", fg='green')

    def _process_input_configs(self):
        """处理输入配置"""
        input_configs = self.task_config['config']['inputs']
        
        # 获取命令行参数
        ctx = click.get_current_context()
        cli_args = getattr(ctx, 'dynamic_args', {})
        
        if self.debug:
            click.secho("\n命令行动态参数:", fg='cyan')
            click.echo(json.dumps(cli_args, ensure_ascii=False, indent=2))
        
        # 处理每个输入配置
        for input_config in input_configs:
            if 'param_name' in input_config and 'node_id' in input_config and 'replace' in input_config:
                param_name = input_config['param_name']
                node_id = str(input_config['node_id'])
                replace_key = input_config['replace'].get('key')
                is_optional = input_config.get('optional', False)
                default_value = input_config.get('default', None)
                
                # 获取参数值（从命令行参数中）
                param_value = None
                if param_name in cli_args:
                    param_value = cli_args[param_name]
                    self.user_params[param_name] = param_value
                
                # 如果参数没有值，检查是否有默认值或是否可选
                if param_value is None:
                    # 先检查是否有默认值，无论参数是否可选
                    if default_value is not None:
                        param_value = default_value
                        self.user_params[param_name] = param_value
                        if self.debug:
                            click.secho(f"使用参数 '{param_name}' 的默认值: {default_value}", fg='yellow')
                    elif is_optional:
                        # 参数是可选的但没有默认值，跳过
                        if self.debug:
                            click.secho(f"跳过可选参数 '{param_name}'", fg='yellow')
                        continue
                    else:
                        # 必填参数，没有默认值，提示用户输入
                        param_value = click.prompt(f"请输入参数 '{param_name}' 的值")
                        self.user_params[param_name] = param_value
                
                # 处理参数值
                if param_value is not None:
                    self._process_param_value(param_name, param_value, node_id, replace_key)

    def _process_param_value(self, param_name, param_value, node_id, replace_key):
        """处理参数值，如果是文件则上传"""
        # 检查是否是本地文件路径（只有字符串类型的参数值才可能是文件路径）
        if isinstance(param_value, str) and os.path.exists(param_value) and os.path.isfile(param_value):
            # 上传文件
            remote_path = self._upload_file(param_value)
            if not remote_path:
                click.secho(f"警告: 文件 '{param_value}' 上传失败", fg='yellow')
                return
                
            self.uploaded_files[param_name] = remote_path
            
            # 更新工作流中的文件路径
            if node_id in self.workflow_data and 'inputs' in self.workflow_data[node_id]:
                if replace_key in self.workflow_data[node_id]['inputs']:
                    # 获取文件名
                    file_name = os.path.basename(remote_path)
                    
                    # 检查节点类型，对LoadImage节点特殊处理
                    is_load_image = False
                    if 'class_type' in self.workflow_data[node_id]:
                        class_type = self.workflow_data[node_id]['class_type']
                        is_load_image = class_type == 'LoadImage'
                        
                    # 对于LoadImage节点，使用完整路径
                    if is_load_image:
                        # 使用完整路径而不是文件名
                        self.workflow_data[node_id]['inputs'][replace_key] = remote_path
                        
                        # 添加调试信息
                        if self.debug:
                            click.secho(f"为LoadImage节点 {node_id} 设置图片完整路径: {remote_path}", fg='green')
                    else:
                        # 非LoadImage节点，直接使用文件名
                        self.workflow_data[node_id]['inputs'][replace_key] = file_name
                        
                    if self.debug:
                        click.secho(f"为节点 {node_id} 设置文件参数 {replace_key}: {file_name if not is_load_image else remote_path}", fg='green')
        else:
            # 非文件参数，直接更新
            # 处理GCS路径（只对字符串类型进行操作）
            if isinstance(param_value, str) and 'gcs://' in param_value:
                param_value = param_value.replace('gcs://', '')
            
            # 更新工作流中的参数值
            if node_id in self.workflow_data and 'inputs' in self.workflow_data[node_id]:
                if replace_key in self.workflow_data[node_id]['inputs']:
                    self.workflow_data[node_id]['inputs'][replace_key] = param_value
                    if self.debug:
                        click.secho(f"为节点 {node_id} 设置参数 {replace_key}: {param_value}", fg='green')

    def _upload_file(self, local_file):
        """上传本地文件到实例"""
        try:
            click.secho(f"正在上传文件 '{local_file}' 到实例...", fg='yellow')
            
            ssh_client, sftp = get_ssh_connection(self.instance_details)
            if not ssh_client or not sftp:
                click.secho("无法建立SSH连接", fg='red')
                return None
                
            # 上传文件
            remote_dir = '/root/netdisk/uploadfiles'
            remote_path = upload_single_file(sftp, local_file, remote_dir)
            
            # 关闭连接
            sftp.close()
            ssh_client.close()
            
            return remote_path
            
        except Exception as e:
            click.secho(f"上传文件失败: {str(e)}", fg='red')
            return None

    def _print_debug_info(self):
        """打印调试信息"""
        if not self.debug:
            return
            
        click.secho("\n工作流数据:", fg='cyan')
        click.echo(json.dumps(self.workflow_data, ensure_ascii=False, indent=2))
        
        # 打印SaveImage节点信息
        click.secho("\nSaveImage节点:", fg='cyan')
        for node_id, node_data in self.workflow_data.items():
            if node_data.get('class_type') == 'SaveImage':
                click.echo(f"节点ID: {node_id}")
                click.echo(json.dumps(node_data, ensure_ascii=False, indent=2))
        
        # 打印用户参数信息
        click.secho("\n用户参数:", fg='cyan')
        for param_name, param_value in self.user_params.items():
            click.echo(f"{param_name}: {param_value}")
        
        # 打印上传文件信息
        if self.uploaded_files:
            click.secho("\n上传文件:", fg='cyan')
            for param_name, file_path in self.uploaded_files.items():
                click.echo(f"{param_name}: {file_path}")
        
        # 打印输出节点信息
        click.secho("\n输出节点信息:", fg='cyan')
        click.echo(f"节点ID: {self.output_node_id}")
        click.echo(f"文件名前缀: {self.output_filename_prefix}")

    def submit_task(self):
        """提交任务到ComfyUI"""
        # 查找ComfyUI端口
        comfyui_endpoint = None
        ports = self.instance_details.get('ports', [])
        cluster_ports = self.instance_details.get('clusterIpPorts', [])
        
        # 先检查ports
        for port in ports:
            if port.get('targetPort') == 8188:
                comfyui_endpoint = port.get('appDomain')
                break
        
        # 如果在ports中没找到，再检查clusterIpPorts
        if not comfyui_endpoint:
            for port in cluster_ports:
                if port.get('appName') and 'comfyui' in port.get('appName', '').lower():
                    comfyui_endpoint = port.get('appDomain')
                    break
        
        if not comfyui_endpoint:
            click.secho("无法找到ComfyUI端点", fg='red')
            return False
        
        # 构建ComfyUI API URL
        comfyui_api_url = f"http://{comfyui_endpoint}/api/prompt"
        
        # 打印完整的工作流数据
        if self.debug:
            click.secho("\n--- 完整的工作流数据 ---", fg='cyan')
            click.echo(f"节点数量: {len(self.workflow_data)}")
            if self.output_node_id:
                click.secho(f"\n输出节点ID: {self.output_node_id}", fg='green')
                if self.output_node_id in self.workflow_data:
                    click.secho("输出节点存在于工作流中", fg='green')
                    click.echo(f"节点信息: {json.dumps(self.workflow_data[self.output_node_id], ensure_ascii=False, indent=2)}")
                else:
                    click.secho(f"警告: 输出节点ID {self.output_node_id} 不在工作流数据中", fg='yellow')
                    click.echo(f"可用的节点ID: {list(self.workflow_data.keys())}")
            
            click.secho("\n工作流的完整数据:", fg='cyan')
            click.echo(json.dumps(self.workflow_data, ensure_ascii=False, indent=2))
        
        # 提交任务到ComfyUI
        click.secho(f"\n正在提交任务到实例 {self.instance_id}...", fg='yellow')
        try:
            with click_spinner.spinner():
                response = requests.post(
                    comfyui_api_url,
                    json={"prompt": self.workflow_data, "client_id": "1"}
                )
                
            if response.status_code != 200:
                click.secho(f"提交任务失败，状态码: {response.status_code}", fg='red')
                click.echo(response.text)
                return False
                
            # 提取任务信息
            result = response.json()
            prompt_id = result.get('prompt_id')
            
            if not prompt_id:
                click.secho("无法获取任务ID", fg='red')
                return False
                
            click.secho(f"任务提交成功！Prompt ID: {prompt_id}", fg='green')
            
            # 生成预期的输出链接
            output_urls = []
            
            # 如果有输出节点配置和文件名前缀，生成预期的输出链接
            if self.output_node_id and self.output_filename_prefix:
                # 获取任务类型
                task_type = os.path.basename(self.task_file).split('.')[0]
                
                # 使用正确的API URL格式
                if task_type == 'removebg':
                    # 使用正确的输出格式，包含api前缀、type和subfolder参数
                    output_urls.append(f"http://{comfyui_endpoint}/api/view?filename={self.output_filename_prefix}_00001_.png&type=output&subfolder=")
                else:
                    # 默认输出格式
                    output_urls.append(f"http://{comfyui_endpoint}/api/view?filename={self.output_filename_prefix}_00001_.png&type=output&subfolder=")
            
            # 打印预期的输出链接
            if output_urls:
                click.secho("\n预期的输出链接:", fg='green')
                for url in output_urls:
                    click.secho(url, fg='cyan')
            
            # 提示实例创建信息
            if self.instance_created:
                click.secho("\n注意：该实例为自动创建，任务完成后不会被删除", fg='yellow')
                click.secho("如需删除该实例，请使用命令:", fg='yellow')
                click.echo(f"hotpod instance delete --id {self.instance_id}")
            
            return True
                
        except requests.exceptions.RequestException as e:
            click.secho(f"请求ComfyUI API失败: {str(e)}", fg='red')
            return False

def create_comfyui_commands(cli):
    """创建ComfyUI命令组"""
    @cli.group('comfyui', cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
    def comfyui():
        """ComfyUI相关命令"""
        pass

    @comfyui.command('runtask', cls=DynamicCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--instance', help='GCS实例ID')
    @click.option('--cluster', help='集群名称')
    @click.option('--task', required=True, help='任务名称或任务配置文件路径')
    @click.option('--debug', is_flag=True, help='启用调试模式')
    @click.pass_context
    def runtask(ctx, instance, cluster, task, debug):
        """运行ComfyUI任务
        
        示例:
        \b
        运行内置任务:
        hotpod comfyui runtask --task objmig
        hotpod comfyui runtask --task removebg
        
        使用指定实例运行任务:
        hotpod comfyui runtask --instance <实例ID> --task objmig
        
        使用指定集群运行任务:
        hotpod comfyui runtask --cluster <集群名称> --task objmig
        
        启用调试模式:
        hotpod comfyui runtask --task objmig --debug
        """
        # 检查参数冲突
        if instance and cluster:
            click.secho("错误: 不能同时指定 --instance 和 --cluster", fg='red')
            return
            
        if debug:
            click.secho("\n命令参数:", fg='cyan')
            click.echo(f"task: {task}")
            click.echo(f"instance: {instance}")
            click.echo(f"cluster: {cluster}")
            click.echo(f"debug: {debug}")
        
        try:    
            comfyui_task = ComfyUITask(task, instance, cluster, debug)
            
            if not comfyui_task.load_task_config():
                return
                
            if not comfyui_task.ensure_instance():
                return
                
            comfyui_task.process_workflow()
            comfyui_task.submit_task()
        except click.ClickException as e:
            # 继续向上抛出 ClickException
            raise e
        except Exception as e:
            # 将其他异常包装为 ClickException
            click.secho(f"执行任务时发生错误: {str(e)}", fg='red')
            if debug:
                import traceback
                click.secho(traceback.format_exc(), fg='red')

    @comfyui.command('createtask', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--name', required=True, help='任务名称')
    @click.option('--raw_api_file', required=True, help='原始API文件路径')
    @click.option('--input_node_id', required=True, help='输入节点ID',multiple=True)
    @click.option('--input_node_name', required=True, help='输入参数名称',multiple=True)
    @click.option('--output_node_id', required=True, help='输出节点ID',multiple=True)
    def createtask(name, raw_api_file, input_node_id, input_node_name, output_node_id):
        """创建ComfyUI任务
        hotpod comfyui createtask --name <任务名称> --raw_api_file <原始API文件路径> --input_node_id <输入节点ID> --input_node_name <输入参数名称> --output_node_id <输出节点ID>
        """
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tasks_dir = os.path.join(current_dir, 'tasks')
                # 检查目录是否存在
        if not os.path.exists(tasks_dir) or not os.path.isdir(tasks_dir):
            click.secho("任务目录不存在", fg='red')
            return
        
        # 获取所有json文件
        task_files = [f for f in os.listdir(tasks_dir) if f.endswith('.json')]
        if name in task_files:
            click.secho(f"错误: 任务 '{name}' 已存在", fg='red')
            return
        
        """创建任务配置文件"""
        task_data = {
            "prompt_template": {},
            "config": {}
        }
        with open(raw_api_file, 'r', encoding='utf-8') as f:
            raw_api_data = json.load(f)
        task_data["prompt_template"] = raw_api_data
        input_list = []
        output_list = []
        for input_node, single_input_node_name in zip(input_node_id, input_node_name):
            node_data = raw_api_data.get(input_node, {})
            config_data = {}
            if node_data.get("inputs"):
                node_type = list(node_data.get("inputs").keys())[0]
                config_data["node_id"] = int(input_node)
                config_data["param_name"] = single_input_node_name
                config_data["replace"] = {
                    "key": node_type,
                    "value": "HOTPOD_INPUT"
                }
                input_list.append(config_data)
            else:
                click.secho(f"错误: 节点 {input_node} 没有输入参数", fg='red')
                return
        for output_node in output_node_id:
            node_data = raw_api_data.get(output_node, {})
            config_data = {}
            if node_data.get("inputs"):
                node_type = list(node_data.get("inputs").keys())[0]
                config_data["node_id"] = int(output_node)
                config_data["param_name"] = node_type
                config_data["replace"] = {
                    "key": node_type,
                    "value": "HOTPOD_UUID"
                }
                output_list.append(config_data)
            else:
                click.secho(f"错误: 节点 {output_node} 没有输入参数", fg='red')
                return
        task_data["config"]["inputs"] = input_list
        task_data["config"]["outputs"] = output_list
        with open(os.path.join(tasks_dir, f"{name}.json"), 'w', encoding='utf-8') as f:
            json.dump(task_data, f, ensure_ascii=False, indent=2)
        click.secho(f"任务 '{name}' 创建成功", fg='green')
                

        
    @comfyui.command('deletetask', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--name', required=True, help='任务名称')
    def deletetask(name):
        """删除任务
        
        示例:
        \b
        删除任务:
        hotpod comfyui deletetask --name <任务名称>
        """
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tasks_dir = os.path.join(current_dir, 'tasks')
        task_file = os.path.join(tasks_dir, f"{name}.json")
        if not os.path.exists(task_file):
            click.secho(f"错误: 任务 '{name}' 不存在", fg='red')
            return
        os.remove(task_file)
        click.secho(f"任务 '{name}' 删除成功", fg='green')

    @comfyui.command('taskinfo', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--task', required=True, help='任务名称')
    def taskinfo(task):
        """显示任务配置信息
        
        示例:
        \b
        查看removebg任务参数:
        hotpod comfyui taskinfo --task removebg
        """
        # 获取tasks目录的路径
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tasks_dir = os.path.join(current_dir, 'tasks')
        task_file = os.path.join(tasks_dir, f"{task}.json")
        
        # 检查任务文件是否存在
        if not os.path.exists(task_file):
            click.secho(f"错误: 任务 '{task}' 不存在", fg='red')
            return
        
        try:
            # 读取任务配置文件
            with open(task_file, 'r', encoding='utf-8') as f:
                task_config = json.load(f)
            
            # 获取config字段中的inputs列表
            if 'config' not in task_config or 'inputs' not in task_config['config']:
                click.secho(f"错误: 任务 '{task}' 的配置文件格式不正确，缺少 config.inputs 字段", fg='red')
                return
                
            inputs = task_config['config']['inputs']
            if not isinstance(inputs, list):
                click.secho(f"错误: 任务 '{task}' 的 config.inputs 字段不是列表格式", fg='red')
                return
                
            # 显示任务信息
            click.secho(f"\n任务 '{task}' 的参数信息:", fg='green', bold=True)
            click.secho("-" * 40, fg='cyan')
            
            # 遍历并显示每个参数
            for input_config in inputs:
                if 'param_name' not in input_config:
                    continue
                    
                param_name = input_config['param_name']
                node_id = input_config.get('node_id', 'N/A')
                replace_info = input_config.get('replace', {})
                key = replace_info.get('key', 'N/A')
                value = replace_info.get('value', 'N/A')
                default_value = input_config.get('default', None)
                is_optional = input_config.get('optional', False)
                
                click.secho(f"参数名: ", fg='cyan', nl=False)
                click.echo(param_name)
                
                # 显示默认值和是否可选
                if default_value is not None:
                    click.secho(f"默认值: ", fg='cyan', nl=False)
                    click.echo(str(default_value))
                
                if is_optional:
                    click.secho(f"可选参数: ", fg='cyan', nl=False)
                    click.echo("是")
                
                # 显示节点和替换信息（可选，用于调试）
                # if True:  # 设置为True显示更多技术细节
                #     click.secho(f"节点ID: ", fg='cyan', nl=False)
                #     click.echo(node_id)
                #     click.secho(f"替换键: ", fg='cyan', nl=False)
                #     click.echo(key)
                #     click.secho(f"替换值: ", fg='cyan', nl=False)
                #     click.echo(value)
                
                # click.echo()  # 添加空行分隔参数
                
            # 显示输出配置信息
            # if 'outputs' in task_config.get('config', {}):
            #     click.secho("\n输出配置:", fg='green', bold=True)
            #     click.secho("-" * 40, fg='cyan')
                
            #     for output_config in task_config['config']['outputs']:
            #         node_id = output_config.get('node_id', 'N/A')
            #         replace_info = output_config.get('replace', {})
            #         key = replace_info.get('key', 'N/A')
            #         value = replace_info.get('value', 'N/A')
                    
            #         click.secho(f"输出节点ID: ", fg='cyan', nl=False)
            #         click.echo(node_id)
            #         click.secho(f"替换键: ", fg='cyan', nl=False)
            #         click.echo(key)
            #         click.secho(f"替换值: ", fg='cyan', nl=False)
            #         click.echo(value)
                    
            #         click.echo()
            
            # 显示使用示例
            click.secho("\n使用示例:", fg='yellow')
            params_example = " ".join([
                f"--{input_config['param_name']} <值>" 
                if 'default' not in input_config else 
                f"--{input_config['param_name']} <值 (默认: {input_config['default']})>"
                for input_config in inputs if 'param_name' in input_config
            ])
            click.echo(f"hotpod comfyui runtask --instance <实例ID> --task {task} {params_example}")
            
        except json.JSONDecodeError:
            click.secho(f"错误: 任务 '{task}' 的配置文件不是有效的JSON格式", fg='red')
        except Exception as e:
            click.secho(f"错误: 读取任务信息时发生错误: {str(e)}", fg='red')

    @comfyui.command('listtask', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    def listtask():
        """列出所有可用的任务
        
        示例:
        \b
        查看所有可用任务:
        hotpod comfyui listtask
        """
        # 获取tasks目录的路径
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tasks_dir = os.path.join(current_dir, 'tasks')
        
        # 检查目录是否存在
        if not os.path.exists(tasks_dir) or not os.path.isdir(tasks_dir):
            click.secho("任务目录不存在", fg='red')
            return
        
        # 获取所有json文件
        task_files = [f for f in os.listdir(tasks_dir) if f.endswith('.json')]
        
        if not task_files:
            click.secho("没有找到任何任务", fg='yellow')
            return
        
        # 显示任务列表
        click.secho("\n可用的任务列表:", fg='green', bold=True)
        click.secho("-" * 40, fg='cyan')
        
        for task_file in task_files:
            task_name = os.path.splitext(task_file)[0]
            
            # 尝试加载任务配置以获取更多信息
            try:
                with open(os.path.join(tasks_dir, task_file), 'r', encoding='utf-8') as f:
                    task_config = json.load(f)
                    
                # 获取任务参数数量
                param_count = 0
                if 'config' in task_config and 'inputs' in task_config['config']:
                    param_count = len(task_config['config']['inputs'])
                    
                click.secho(f"{task_name}", fg='cyan', nl=False)
                click.echo(f" ({param_count} 个参数)")
                    
            except Exception:
                # 如果无法读取配置，只显示任务名
                click.secho(f"{task_name}", fg='cyan')
        
        # 显示使用说明
        click.secho("\n使用任务示例:", fg='yellow')
        click.echo("hotpod comfyui runtask --task <任务名称>")
        click.echo("查看任务详情: hotpod comfyui taskinfo --task <任务名称>")

    return comfyui

# 用于直接在main.py中创建命令组的函数
def create_comfyui_group(cli):
    """创建ComfyUI命令组供main.py使用"""
    return create_comfyui_commands(cli) 