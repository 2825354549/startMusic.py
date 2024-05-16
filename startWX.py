# User: 廖宇
# Date Development：2024/5/10 15:55
# D:\WeChat
import subprocess
from pywinauto.application import Application
import time
import time
from pytesseract import pytesseract
from pywinauto.application import Application
from pywinauto import Desktop
import pyautogui


# 微信程序的路径
# wechat_path = 'D:\WeChat\WeChat.exe'
# 网易云音乐程序的路径
# netease_cloud_music_path = 'C:\\Program Files (x86)\\Netease\\CloudMusic\\cloudmusic.exe'

# 启动微信
# subprocess.Popen(wechat_path)


    # def startwx(self):
    #
    #     # 设置Tesseract的路径
    #     pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #
    #     # 启动微信应用程序
    #     app = Application(backend="uia").start('D:\\WeChat\\WeChat.exe')
    #
    #     # 等待微信窗口出现
    #     time.sleep(10)
    #
    #     # 连接到微信窗口
    #     wechat_window = app.window(title_re=".*微信.*")
    #     wechat_window.wait('ready', timeout=20)
    #
    #     # 截取当前屏幕
    #     screenshot = pyautogui.screenshot()
    #
    #     # 使用pytesseract识别屏幕上的文字
    #     text = pytesseract.image_to_string(screenshot)
    #
    #     # 查找“进入微信”文字的位置
    #     if "进入微信" in text:
    #         # 获取“进入微信”按钮的坐标
    #         for window in Desktop(backend="uia").windows():
    #             if "进入微信" in window.window_text():
    #                 rect = window.rectangle()
    #                 x = rect.mid_point().x
    #                 y = rect.mid_point().y
    #                 # 点击“进入微信”按钮
    #                 pyautogui.click(x, y)
    #                 break
class StartWX():
    def start_wx(self):
        # 启动微信
        app = Application(backend="uia").start('D:\\WeChat\\WeChat.exe')

        # 等待程序启动和窗口出现
        time.sleep(1)

        # 连接到微信窗口
        wechat_window = app.window(title_re=".*微信.*")

        # 等待窗口响应
        wechat_window.wait('ready', timeout=2)

        # 执行点击操作，这里需要根据实际情况来定位按钮
        # 例如，如果要点击的按钮有一个特定的控件ID或文本
        # wechat_window.child_window(control_id=控件ID, title="按钮文本").click()

        # 如果不确定控件的详细信息，可以使用窗口的print_control_identifiers()方法来获取
        # wechat_window.print_control_identifiers()
        # enter_wechat_button = wechat_window['进入微信']
        # enter_wechat_button.click()
        # 使用.click_input()方法点击“进入微信”按钮
        enter_wechat_button = wechat_window.child_window(title="进入微信", control_type="Button")
        enter_wechat_button.click_input()


if __name__ == '__main__':
    StartWX().start_wx()
