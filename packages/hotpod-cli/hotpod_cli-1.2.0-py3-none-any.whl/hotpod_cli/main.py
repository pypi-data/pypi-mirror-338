"""HotPod CLI 主入口模块"""

import os
import sys
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from dotenv import load_dotenv

from .commands.instance import create_instance_group
from .commands.file import create_file_group
from .commands.comfyui import create_comfyui_group
from .commands.llm import create_llm_group
from .commands.cluster import create_cluster_group

# 加载.env文件
load_dotenv()


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green',
    context_settings=dict(help_option_names=['-h', '--help'])
)
def cli():
    """HotPod CLI - GCS命令行工具"""
 
    required_env_vars = ['JDCLOUD_AK', 'JDCLOUD_SK']
    missing_env_vars = [var for var in required_env_vars if not os.environ.get(var)]
    
    if missing_env_vars:
        click.secho(f"错误: 缺少必要的环境变量: {', '.join(missing_env_vars)}", fg='red')
        click.secho("请在.env文件中设置以下变量:", fg='yellow')
        click.secho("  JDCLOUD_AK - 京东云访问密钥ID", fg='yellow')
        click.secho("  JDCLOUD_SK - 京东云秘密访问密钥", fg='yellow')
        click.secho("\n或者通过环境变量设置:", fg='green')
        click.secho("  export JDCLOUD_AK=your_access_key", fg='cyan')
        click.secho("  export JDCLOUD_SK=your_secret_key", fg='cyan')
        sys.exit(1)


@cli.command('info', cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='green')
def info():
    """显示HotPod CLI的信息"""
    click.secho("HotPod CLI", fg='green', bold=True)
    click.secho("HotPod命令行工具", fg='white')
    click.secho("\n开发者: hong", fg='cyan')
    click.secho("版本: 1.1.1", fg='cyan')


def create_app():
    """创建完整的CLI应用
    
    Returns:
        函数对象: CLI主函数，可以作为命令行入口点
    """
    # 创建命令组
    instance_group = create_instance_group(cli)
    file_group = create_file_group(cli)
    comfyui_group = create_comfyui_group(cli)
    llm_group = create_llm_group(cli)
    cluster_group = create_cluster_group(cli)
    
    return cli


# 提供一个简单的入口点函数
def main():
    """命令行工具的主入口点"""
    create_app()()


if __name__ == '__main__':
    main() 