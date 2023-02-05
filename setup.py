import moviepy.editor as mp
import cv2
import os

file = "computer.gif"
# path to the folder we are saving frames to
path = os.path.join(os.getcwd(), 'temp\\')

# path to gif
gif_path = os.path.join(os.getcwd(), 'gifs\\', file)

# do not change this unless you want to change other things in the script
video_file = "1.mp4"


# gif to videoclip
clip = mp.VideoFileClip(os.path.join(gif_path))
clip.write_videofile(os.path.join(path, video_file))

video_path = os.path.join(path, video_file)

def extract_frames():
    # get frame_count
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # now extract frames
    cap = cv2.VideoCapture(video_path)
    count = 1
    for x in range(frame_count):
        save = path + str(x) + ".jpg"
        ret, frame = cap.read()
        cv2.imwrite(save, frame)
        count += 1

    return frame_count, round(clip.duration / frame_count, 2)

extract_frames()
