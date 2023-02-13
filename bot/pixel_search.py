from PIL import ImageGrab
import cv2
import numpy as np

im = ImageGrab.grab(bbox=(565, 27, 1073, 357))
opencvImage = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
# im = cv2.imread('test.png')
# im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
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
