"""Click工具类和函数"""

from click_help_colors import HelpColorsCommand


class DynamicCommand(HelpColorsCommand):
    """支持动态参数的命令类
    
    这个类允许处理命令行中未预先定义的参数，
    特别适用于那些参数名是动态的情况
    """
    
    def __init__(self, *args, **kwargs):
        """初始化动态命令类"""
        super().__init__(*args, **kwargs)
        self.ignore_unknown_options = True
        self.allow_extra_args = True
        
    def parse_args(self, ctx, args):
        """解析命令行参数
        
        Args:
            ctx: Click上下文对象
            args: 命令行参数列表
            
        Returns:
            解析结果
        """
        # 先处理已知的参数
        ctx.args = args
        args, dynamic_args = self._parse_dynamic_args(args)
        ctx.dynamic_args = dynamic_args
        return super().parse_args(ctx, args)
    
    def _parse_dynamic_args(self, args):
        """从参数列表中提取动态参数
        
        Args:
            args: 命令行参数列表
            
        Returns:
            (remaining_args, dynamic_args) 元组
        """
        # 定义已知的固定参数列表
        known_params = {'instance', 'task', 'help', 'cluster', 'debug'}
        
        remaining_args = []
        dynamic_args = {}
        i = 0
        while i < len(args):
            if args[i].startswith('--'):
                param = args[i][2:]  # 去掉前面的--
                # 检查我们是否知道这个参数
                if param in known_params:
                    remaining_args.append(args[i])
                    if i + 1 < len(args) and not args[i + 1].startswith('--'):
                        remaining_args.append(args[i + 1])
                        i += 2
                    else:
                        i += 1
                else:
                    # 这是一个动态参数
                    if i + 1 < len(args) and not args[i + 1].startswith('--'):
                        dynamic_args[param] = args[i + 1]
                        i += 2
                    else:
                        dynamic_args[param] = True
                        i += 1
            else:
                remaining_args.append(args[i])
                i += 1
        return remaining_args, dynamic_args 