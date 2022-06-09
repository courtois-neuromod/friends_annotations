import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from typing import Iterable, List, Tuple


def calculate_frame_score(current_frame_hsv: Iterable[np.ndarray],
                          last_frame_hsv: Iterable[np.ndarray]) -> Tuple[float]:
    """Calculates score between two adjacent frames in the HSV colourspace. Frames should be
    split, e.g. cv2.split(cv2.cvtColor(frame_data, cv2.COLOR_BGR2HSV)).
    Arguments:
        curr_frame_hsv: Current frame.
        last_frame_hsv: Prevdf = pd.DataFrame(my_array, columns = ['Column_A','Column_B','Column_C'])
ious frame.
    Returns:
        Tuple containing the average pixel change for each component as well as the average
        across all components, e.g. (avg_h, avg_s, avg_v, avg_all).
    """
    current_frame_hsv = [x.astype(np.int32) for x in current_frame_hsv]
    last_frame_hsv = [x.astype(np.int32) for x in last_frame_hsv]
    delta_hsv = [0, 0, 0, 0]
    for i in range(3):
        num_pixels = current_frame_hsv[i].shape[0] * current_frame_hsv[i].shape[1]
        delta_hsv[i] = np.sum(
            np.abs(current_frame_hsv[i] - last_frame_hsv[i])) / float(num_pixels)

    delta_hsv[3] = sum(delta_hsv[0:3]) / 3.0
    return tuple(delta_hsv)


diff = []
d = 0


vidfile = 'friends_s01e01.mkv'
cap = cv2.VideoCapture(vidfile)
file_name = vidfile[:-4]
frames = [np.inf, np.inf]
# frames = np.empty(2)

# Code sample iterates through all frames, might be too taxing to append all frames to one list...

success = True
a = True
b = False
# while d< num_frames-1:
#     c = calculate_frame_score(frames[d], frames2[d])
#     diff.append(c)
#     d+=1


while success:
    success, image = cap.read()
    if success:
        if a:
            frames[0] = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
            a = False
        if b:
            frames[1] = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
            c = calculate_frame_score(frames[1], frames[0])
            diff.append(c)
            frames[0] = frames[1]
        b = True


df = pd.DataFrame(diff, columns = ['Hue','Saturation', 'Luminance', 'Average'])
df.to_csv('HSV_values_'+file_name+ '.csv')
