# User: 廖宇
# Date Development：2024/5/10 13:46
import sys
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from startWhale import StartWhale
from startWX import StartWX
from startMusic import StartMusic
import ctypes

class StartAll():
    def __init__(self):
        # 检查是否有管理员权限
        # 检查是否有管理员权限
        try:
            if not self.is_admin():
                # 如果不是管理员，尝试以管理员身份重新启动脚本
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit()  # 退出当前的脚本执行
        except Exception as e:
            print(f"检查管理员权限时发生错误: {e}")
            sys.exit(1)
        # # 创建实例
        # self.net = TestStartnet()
        self.whale = StartWhale()
        self.wx = StartWX()
        self.music = StartMusic()

    def is_admin(self):
        """检查当前用户是否是管理员"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def start_net(self):
        # 通过实例调用方法
        # self.net.test_start_net()
        # pass
        self.driver = webdriver.Chrome()
        self.vars = {}

        # 尝试执行测试步骤
        try:
            # Test name: start_net
            # Step # | name | target | value
            # 1 | open | / |
            self.driver.get("http://10.2.5.251/")
            self.driver.set_window_size(1032, 995)
            # 使用JavaScript来执行点击操作，不受元素遮挡的影响
            element = self.driver.find_element(By.CSS_SELECTOR, ".edit_lobo_cell:nth-child(2)")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

            self.driver.find_element(By.CSS_SELECTOR, ".edit_lobo_cell:nth-child(2)").send_keys("TS22060150P31")

            self.driver.find_element(By.CSS_SELECTOR, ".edit_lobo_cell:nth-child(3)").send_keys("WDSRwdsr19990704")
            element2 = self.driver.find_element(By.NAME, "ISP_select")
            self.driver.execute_script("arguments[0].click();", element2)
            dropdown = self.driver.find_element(By.NAME, "ISP_select")
            dropdown.find_element(By.XPATH, "//option[. = '中国移动']").click()
            element3 = self.driver.find_element(By.CSS_SELECTOR, ".edit_lobo_cell:nth-child(1)")
            self.driver.execute_script("arguments[0].click();", element3)
            # print('network start')

        # 捕获并打印任何异常
        except Exception as e:
            print(f"测试过程中发生错误: {e}")

        # 测试完成后关闭浏览器
        finally:
            self.driver.close()
            # 退出WebDriver
            self.driver.quit()

    def start_whale(self):
        try:
            self.whale.auto_whale()
        except Exception as e:
            print(f"启动Whale时发生错误: {e}")

    def start_wx(self):
        try:
            self.wx.start_wx()
        except Exception as e:
            print(f"启动微信时发生错误: {e}")

    def start_music(self):
        try:
            self.music.start_music()
        except Exception as e:
            print(f"启动网易云音乐时发生错误: {e}")

    def start_all(self):
        try:
            self.start_net()
            sleep(1)
            self.start_whale()
            sleep(1)
            self.start_wx()
            sleep(1)
            self.start_music()
        except Exception as e:
            print(f"执行start_all时发生错误: {e}")

if __name__ == '__main__':
    try:
        start_all = StartAll()
        start_all.start_all()
    except Exception as e:
        print(f"初始化StartAll或执行start_all时发生错误: {e}")