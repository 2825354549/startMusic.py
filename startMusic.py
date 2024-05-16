# User: 廖宇
# Date Development：2024/5/10 16:37
import os
class StartMusic():
    def start_music(self):
        path = 'E:\网易音乐\CloudMusic\cloudmusic.exe'
        # 使用os模块的startfile方法启动网易云音乐
        os.startfile(path)

if __name__ == '__main__':
    startmusic = StartMusic()
    startmusic.start_music()
