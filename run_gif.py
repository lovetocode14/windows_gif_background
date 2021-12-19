import time
import ctypes

# path to folder that contains the .jpg that were converted 
path = ""




def play_gif():
    while True:
        for x in range(603):
            time.sleep(0.057)

            run_path = path + str(x) + ".jpg"
            ctypes.windll.user32.SystemParametersInfoW(20, 0, run_path, 1)


play_gif()
