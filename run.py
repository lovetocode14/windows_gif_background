import os
import time
import ctypes
import setup


info = setup.extract_frames()
path = os.path.join(os.getcwd(), 'temp\\')


def play():
    while True:
        for i in range(info[0]):
            run_path = path + str(i) + ".jpg"
            ctypes.windll.user32.SystemParametersInfoW(20, 0, run_path , 1)
            time.sleep(info[1])

play()

