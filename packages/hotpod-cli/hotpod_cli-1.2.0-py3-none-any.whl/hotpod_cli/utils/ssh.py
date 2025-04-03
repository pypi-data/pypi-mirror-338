"""SSH和SFTP相关工具函数"""

import os
import click
import click_spinner
import paramiko


def ensure_remote_dir(sftp, remote_dir):
    """确保远程目录存在，如果不存在则创建
    
    Args:
        sftp: SFTP客户端
        remote_dir: 远程目录路径
    """
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


def upload_single_file(sftp, local_file, remote_dir):
    """上传单个文件到远程目录
    
    Args:
        sftp: SFTP客户端
        local_file: 本地文件路径
        remote_dir: 远程目录
        
    Returns:
        远程文件路径
    """
    ensure_remote_dir(sftp, remote_dir)
    
    file_name = os.path.basename(local_file)
    remote_file_path = os.path.join(remote_dir, file_name)
    
    click.secho(f"正在上传文件: {file_name}...", fg='yellow')
    with click_spinner.spinner():
        sftp.put(local_file, remote_file_path)
    
    click.secho("文件上传成功！", fg='green')
    click.secho(f"文件位置: {remote_file_path}", fg='cyan')
    
    return remote_file_path


def upload_directory(sftp, local_dir, remote_base_dir):
    """递归上传目录及其内容到远程目录
    
    Args:
        sftp: SFTP客户端
        local_dir: 本地目录路径
        remote_base_dir: 远程基础目录
        
    Returns:
        上传文件数量，远程目录路径
    """
    # 获取本地目录的基名
    dir_name = os.path.basename(local_dir.rstrip('/'))
    remote_dir = os.path.join(remote_base_dir, dir_name)
    
    # 确保远程目标目录存在
    ensure_remote_dir(sftp, remote_dir)
    
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
            ensure_remote_dir(sftp, current_remote_dir)
        
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
    
    return uploaded_files, remote_dir


def get_ssh_connection(instance_details):
    """从实例详情中获取SSH连接信息并创建连接
    
    Args:
        instance_details: 实例详情字典
        
    Returns:
        (ssh_client, sftp_client) 元组，失败时返回 (None, None)
    """
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
        return None, None
    
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
        return ssh, sftp
        
    except paramiko.AuthenticationException:
        click.secho("错误: SSH认证失败，请检查用户名和密码", fg='red')
    except paramiko.SSHException as e:
        click.secho(f"错误: SSH连接错误: {str(e)}", fg='red')
    except Exception as e:
        click.secho(f"连接过程中发生错误: {str(e)}", fg='red')
        
    return None, None 