"""文件操作相关命令模块"""

import os
import click
import click_spinner
from click_help_colors import HelpColorsGroup, HelpColorsCommand

from ..gcs import GCS
from ..utils.ssh import get_ssh_connection, upload_single_file, upload_directory


def create_file_group(cli):
    """创建文件命令组
    
    Args:
        cli: CLI主命令组
        
    Returns:
        文件命令组
    """
    @cli.group('fs', cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='green')
    def fs():
        """管理实例上的文件"""
        pass
    
    @fs.command('upload', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    @click.option('--instance', required=True, help='GCS实例ID')
    @click.option('--local', required=True, type=click.Path(exists=True), help='本地文件路径，以/结尾表示上传整个文件夹')
    @click.option('--remote', default='/root/netdisk', help='远程文件路径')
    def file_upload(instance, local, remote):
        """上传文件到实例"""
        click.echo(f"获取实例 {instance} 的详细信息...")
        
        # 获取实例信息
        gcs = GCS()
        response = gcs.get_instance(instance)
        if not response or 'instance' not in response:
            click.secho("未找到指定实例", fg='red')
            return
            
        # 获取真正的实例信息，在instance键下
        instance_details = response.get('instance', {})
        
        # 检查实例状态
        status = instance_details.get('status')
        if status != 'running':
            click.secho(f"实例 {instance} 未运行。当前状态: {status}", fg='red')
            return
        
        click.echo("正在连接到实例...")
        # 创建SSH连接
        try:
            # 获取SSH和SFTP客户端
            ssh_client, sftp_client = get_ssh_connection(instance_details)
            if not ssh_client or not sftp_client:
                click.secho("连接实例失败", fg='red')
                return
            
            click.echo("正在连接到远程服务器...")
            try:
                # 检查是否上传整个文件夹
                is_directory = local.endswith('/') or os.path.isdir(local)
                
                if is_directory:
                    # 上传文件夹
                    click.secho(f"正在上传目录 {local} 到 {remote}...", fg='yellow')
                    upload_count, remote_dir = upload_directory(sftp_client, local, remote)
                    click.secho(f"目录上传完成！共上传 {upload_count} 个文件到 {remote_dir}", fg='green')
                else:
                    # 获取远程文件名
                    remote_filename = os.path.basename(local)
                    remote_path = f"{remote}/{remote_filename}"
                    
                    # 上传文件
                    click.secho(f"正在上传文件 {local} 到 {remote_path}...", fg='yellow')
                    sftp_client.put(local, remote_path)
                    click.secho(f"文件上传成功: {remote_path}", fg='green')
                
            except Exception as e:
                click.secho(f"SFTP操作失败: {str(e)}", fg='red')
            
            finally:
                # 关闭连接
                sftp_client.close()
                ssh_client.close()
                
        except Exception as e:
            click.secho(f"SSH连接失败: {str(e)}", fg='red')
    
    # @fs.command('exec', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    # @click.option('--instance', required=True, help='GCS实例ID')
    # @click.option('--cmd', required=True, help='要执行的命令')
    # def file_exec(instance, cmd):
    #     """在GCS实例上执行命令"""
    #     click.secho(f"获取实例 {instance} 的详细信息...", fg='yellow')
    #     gcs = GCS()
        
    #     # 获取实例详情
    #     with click_spinner.spinner():
    #         response = gcs.get_instance(instance)
            
    #     if not response or 'instance' not in response:
    #         click.secho(f"无法获取实例 {instance} 的详细信息", fg='red')
    #         return
            
    #     instance_details = response.get('instance', {})
        
    #     # 检查实例状态
    #     status = instance_details.get('status')
    #     if status != 'running':
    #         click.secho(f"实例 {instance} 未运行。当前状态: {status}", fg='red')
    #         return
            
    #     # 建立SSH连接
    #     click.secho("正在连接到实例...", fg='yellow')
        
    #     try:
    #         ssh_client = get_ssh_connection(instance_details)
    #     except Exception as e:
    #         click.secho(f"连接实例失败: {str(e)}", fg='red')
    #         return
        
    #     try:
    #         # 执行命令
    #         click.secho(f"执行命令: {cmd}", fg='yellow')
    #         stdin, stdout, stderr = ssh_client.exec_command(cmd)
            
    #         # 获取输出
    #         stdout_text = stdout.read().decode('utf-8')
    #         stderr_text = stderr.read().decode('utf-8')
            
    #         # 显示输出
    #         if stdout_text:
    #             click.secho("命令输出:", fg='green')
    #             click.echo(stdout_text)
                
    #         if stderr_text:
    #             click.secho("命令错误:", fg='red')
    #             click.echo(stderr_text)
            
    #         # 获取退出状态
    #         exit_status = stdout.channel.recv_exit_status()
    #         if exit_status == 0:
    #             click.secho("命令执行成功", fg='green')
    #         else:
    #             click.secho(f"命令执行失败，退出状态码: {exit_status}", fg='red')
                
    #     except Exception as e:
    #         click.secho(f"执行命令失败: {str(e)}", fg='red')
    #     finally:
    #         # 关闭连接
    #         ssh_client.close()
    #         click.secho("连接已关闭", fg='yellow')
            
    # @fs.command('list', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    # @click.option('--instance', required=True, help='GCS实例ID')
    # @click.option('--path', default='/root', help='要列出内容的远程目录路径')
    # def file_list(instance, path):
    #     """列出GCS实例上的文件和目录"""
    #     click.secho(f"获取实例 {instance} 的详细信息...", fg='yellow')
    #     gcs = GCS()
        
    #     # 获取实例详情
    #     with click_spinner.spinner():
    #         response = gcs.get_instance(instance)
            
    #     if not response or 'instance' not in response:
    #         click.secho(f"无法获取实例 {instance} 的详细信息", fg='red')
    #         return
            
    #     instance_details = response.get('instance', {})
        
    #     # 检查实例状态
    #     status = instance_details.get('status')
    #     if status != 'running':
    #         click.secho(f"实例 {instance} 未运行。当前状态: {status}", fg='red')
    #         return
            
    #     # 建立SSH连接
    #     click.secho("正在连接到实例...", fg='yellow')
        
    #     try:
    #         ssh_client = get_ssh_connection(instance_details)
    #     except Exception as e:
    #         click.secho(f"连接实例失败: {str(e)}", fg='red')
    #         return
        
    #     try:
    #         # 执行ls命令列出文件
    #         cmd = f"ls -la {path}"
    #         click.secho(f"执行命令: {cmd}", fg='yellow')
    #         stdin, stdout, stderr = ssh_client.exec_command(cmd)
            
    #         # 获取输出
    #         stdout_text = stdout.read().decode('utf-8')
    #         stderr_text = stderr.read().decode('utf-8')
            
    #         # 显示输出
    #         if stdout_text:
    #             click.secho(f"\n{path} 目录内容:", fg='green')
    #             click.echo(stdout_text)
                
    #         if stderr_text:
    #             click.secho("命令错误:", fg='red')
    #             click.echo(stderr_text)
            
    #     except Exception as e:
    #         click.secho(f"列出文件失败: {str(e)}", fg='red')
    #     finally:
    #         # 关闭连接
    #         ssh_client.close()
    #         click.secho("连接已关闭", fg='yellow')
    
    # @fs.command('download', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
    # @click.option('--instance', required=True, help='GCS实例ID')
    # @click.option('--remote', required=True, help='远程文件路径')
    # @click.option('--local', default='.', help='本地保存路径')
    # def file_download(instance, remote, local):
    #     """从GCS实例下载文件"""
    #     click.secho(f"获取实例 {instance} 的详细信息...", fg='yellow')
    #     gcs = GCS()
        
    #     # 获取实例详情
    #     with click_spinner.spinner():
    #         response = gcs.get_instance(instance)
            
    #     if not response or 'instance' not in response:
    #         click.secho(f"无法获取实例 {instance} 的详细信息", fg='red')
    #         return
            
    #     instance_details = response.get('instance', {})
        
    #     # 检查实例状态
    #     status = instance_details.get('status')
    #     if status != 'running':
    #         click.secho(f"实例 {instance} 未运行。当前状态: {status}", fg='red')
    #         return
            
    #     # 建立SSH连接
    #     click.secho("正在连接到实例...", fg='yellow')
        
    #     try:
    #         ssh_client = get_ssh_connection(instance_details)
    #     except Exception as e:
    #         click.secho(f"连接实例失败: {str(e)}", fg='red')
    #         return
            
    #     try:
    #         sftp = ssh_client.open_sftp()
    #         click.secho("SFTP连接已建立", fg='green')
            
    #         # 检测目标目录是否存在
    #         if not os.path.exists(local):
    #             os.makedirs(local)
    #             click.secho(f"已创建本地目录: {local}", fg='yellow')
            
    #         # 提取远程文件名
    #         remote_filename = os.path.basename(remote)
    #         local_path = os.path.join(local, remote_filename) if os.path.isdir(local) else local
            
    #         # 下载文件
    #         click.secho(f"正在下载 {remote} 到 {local_path}...", fg='yellow')
            
    #         try:
    #             with click_spinner.spinner():
    #                 sftp.get(remote, local_path)
    #             click.secho(f"文件下载成功: {local_path}", fg='green')
    #         except FileNotFoundError:
    #             click.secho(f"远程文件不存在: {remote}", fg='red')
    #         except Exception as e:
    #             click.secho(f"下载文件失败: {str(e)}", fg='red')
    #     except Exception as e:
    #         click.secho(f"SFTP操作失败: {str(e)}", fg='red')
    #     finally:
    #         # 关闭连接
    #         if 'sftp' in locals():
    #             sftp.close()
    #         ssh_client.close()
    #         click.secho("连接已关闭", fg='yellow')

    return fs 