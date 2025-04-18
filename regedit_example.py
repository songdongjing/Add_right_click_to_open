from tools.add_right_click import add_open_directory, add_open_background
import sys
import ctypes
import argparse

def is_admin():
    """
    检查是否具有管理员权限
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """
    以管理员权限重新运行程序
    """
    if not is_admin():
        # 重新以管理员权限运行
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def parse_arguments():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(description='添加右键菜单项')
    parser.add_argument('--path', '-p', required=True, help='程序路径')
    parser.add_argument('--name', '-n', required=True, help='右键菜单显示名称')
    parser.add_argument('--directory', '-d', action='store_true', help='是否添加打开文件夹')
    parser.add_argument('--background', '-b', action='store_true', help='是否添加空白处打开')
    return parser.parse_args()

if __name__ == "__main__":
    # 解析命令行参数
    args = parse_arguments()
    
    # 检查并请求管理员权限
    run_as_admin()
    
    # 添加右键菜单
    if args.background:
        add_open_directory(args.path, args.name)
    if args.background:
        add_open_background(args.path, args.name)