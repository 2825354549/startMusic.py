# User: 廖宇
# Date Development：2024/5/10 14:47
import ctypes
import os
import subprocess
import sys
import time

from pywinauto import Application


class StartWhale():
    def open_file_manager_and_execute(self):
        # 打开文件管理器并导航到D盘的‘加速器’文件夹
        folder_path = os.path.join('D:\\', '加速器')
        subprocess.run(['explorer', folder_path], check=True)
        # 等待文件管理器打开
        time.sleep(1)
        # # 执行'Whale.exe'程序
        whale_exe_path = os.path.join(folder_path, 'Whale.exe')
        print('22222')
        if os.path.exists(whale_exe_path):
            subprocess.run([whale_exe_path], check=True)
            # 使用runas命令以管理员权限启动Whale.exe
            print('1111')
            # subprocess.Popen(['runas', '/user:Administrator', whale_exe_path])
        else:
            print(f"未找到文件: {whale_exe_path}")

        # 等待程序启动
        time.sleep(2)

        # 这里假设'Whale.exe'在启动时会弹出一个对话框，并且'是'按钮是默认选项
        # 模拟按下'Enter'键以选择'是'
        subprocess.run(['cmd', '/c', 'echo', '|', 'set', '/p', '=', '""', '>', 'nul'], check=True)
    def start_whale(self):
        path = 'D:\加速器\Whale.exe'
        os.startfile(path)

    def auto_whale(self):
        # 启动
        app = Application(backend="uia").start('D:\加速器\Whale.exe')

        # 等待程序启动和窗口出现
        time.sleep(3)

        # 连接到窗口
        wechat_window = app.window(title_re=".*Whale.exe.*")

        # 等待窗口响应
        wechat_window.wait('ready', timeout=2)

        enter_wechat_button = wechat_window.child_window(title="是", control_type="Button")
        enter_wechat_button.click_input()
        time.sleep(3)


# 检查是否有管理员权限的函数
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
#
# # 如果不是管理员，请求提升权限
# if not is_admin():
#     script_path = os.path.abspath(sys.argv[0])
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1)
#     sys.exit()

if __name__ == '__main__':
    # 创建StartWhale类的实例
    whale_starter = StartWhale()
    # print('3333')

    # 调用方法以启动程序
    whale_starter.auto_whale()
