import cv2
import numpy as np
import math

filename = ['','','','']

M = np.array([[0.412453, 0.357580, 0.180423],
              [0.212671, 0.715160, 0.072169],
              [0.019334, 0.119193, 0.950227]]) 

def f(t):
    if (t > (6/29)**3):
        t = t**(1/3)
    else:
        t = 1/3*((29/6)**2)*t + 4/29
def rgb2lab(pixel):
    b,g,r = pixel[0], pixel[1], pixel[2]
    rgb = np.array([r, g, b])
    xyz = np.dot(M, rgb.T)
    xyz = xyz / 255
    x = xyz[0] / 0.95047
    y = xyz[1]
    z = xyz[2] / 1.08883
    for i in xyz:
        f_x = f(i)
        if(y > )
if __name__ == '__main__':
    img = cv2.imread(i)
    row = img.shape[0]
    col = img.shape[1]
    img_new = np.zeros((w,h,3))
    lab = np.zeros((w,h,3))
    for i in range(row):
        for j in range(col):
            Lab_img = rgb2lab(img[i,j])
            lab[i,j] = (Lab[0], Lab[1], Lab[2])
