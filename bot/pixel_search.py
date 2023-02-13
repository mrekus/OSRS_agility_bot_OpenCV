from PIL import ImageGrab
import cv2
import numpy as np


def get_coordinates(bbox=(565, 27, 1073, 357)):
    im = ImageGrab.grab()
    opencvImage = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    coord = list()
    for j in range(0, opencvImage.shape[0]):
        for i in range(0, opencvImage.shape[1]):
            if opencvImage[j][i].tolist() == [0, 255, 0]:
                coord.append([j, i])
                print(coord[0])
                break
        else:
            continue
        break
    return coord[0][0], coord[0][1]
