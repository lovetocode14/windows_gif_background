import time
import ctypes

# path to folder that contains the .jpg that were converted 
path = ""
number_of_frames = 0
avg_frame_duration = 0




def play_gif():
    while True:
        for x in range(number_of_frames):
            time.sleep(average_frame_duration)

            run_path = path + str(x) + ".jpg"
            ctypes.windll.user32.SystemParametersInfoW(20, 0, run_path, 1)


play_gif()
