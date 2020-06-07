from PIL import Image
import math
import numpy as np

filename = ['', '' ,'' ,'']

def hiseq(v,row,col):
    cdfMAX = row *col
    freq = [0] * 256  
    cdf = [0] * 256 
    for i in range(row):
        for j in range(col):
            freq[v[i * col + j]] = freq[v[i * col + j]] + 1
    prevSum = 0
    find = 0
    return_list = []
    for i in range(256):
        prevSum += freq[i] 
        cdf[i] = prevSum
        if prevSum != 0 and find != 1:
            min = prevSum
            find = 1
    for i in range(row):
        for j in range(col):
            return_list.append(int(round(255 * (cdf[ v[i * col + j] ] - min) /  (cdfMAX-min ))))
    return return_list
def rgbtohsi(r, g, b):
    r = r / 255
    g = g / 255
    b = b / 255
    num = 0.5 * ((r - g) + (r - b))
    den = ((r - g) * (r - g) + (r - b) * (g - b)) ** (0.5)
    if (b <= g):

        if den != 0:
            h = math.acos(num / (den))
        else:
            h = 0
    elif (b > g):
        if den != 0:
            h = (2 * math.pi) - math.acos(num / den)
        else:
            h = 0
    if(r + g + b == 0):
        s=0
    else:
        s = 1 - (3 * min(r, g, b) / (r + g + b))
    i = (r + g + b) / 3
    return int(h * 255), int(s * 255), int(i * 255)
def hsitorgb(h, s, v):
    h = h / 255
    s = s / 255
    v = v / 255
    h = h * 2 * math.pi
    num = s * math.cos(h)
    den = math.cos( (math.pi / 3) - h)
    if (h < 2/3*math.pi):
        b = v * (1 - s)
        if (den == 0):
            r = 0
        else:
            r = (1 + (den - num)) * v
        g = 3 * v - (r + b)
    elif (h > 2/3*math.pi and h < math.pi):
        h = h - (2/3*math.pi)
        r = v*(1-s)
        g = (1 + (den - num)) * v
        b = 3 * v - (r + g)
    else:
        h = h - (4/3*math.pi)
        g = v*(1-s)
        b = (1 + (den - num)) * v
        r = 3 * v - (b + g)
    return int(r*250) ,int(g*255) ,int(b*255)
img = Image.open("aloe.jpg").convert("RGB")
img.show()
img1 = img.copy()
img2 = img.copy()
pixel = img1.load()
row = img.size[0]
col = img.size[1]
for i in range(row):
    for j in range(col):
        r, g, b = img1.getpixel((i, j))
        (h, s, v) = rgbtohsi(r, g, b)
        img1.putpixel((i,j) , (h, s, v))
img1.show()
h_list = []
s_list = []
i_list = []
#print(pixel)
for i in range(row):
    for j in range(col):
            h_list.append(pixel[i,j][0])
            s_list.append(pixel[i,j][1])
            i_list.append(pixel[i,j][2])
array = np.array(i_list)
i_list = hiseq(array,row,col)
#pixel2 = img2.load()
for i in range(row):
    for j in range(col):
        img2.putpixel((i , j),(h_list[i * col + j], s_list[i * col + j], i_list[i * col + j]) )
img2.show()
for i in range(row):
    for j in range(col):
        h, s, v = img2.getpixel((i, j))
        (r, g, b) = hsitorgb(h, s, v)
        img2.putpixel((i,j) , (r, g, b))
img2.show()
