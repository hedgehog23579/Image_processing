from PIL import Image
import math
import numpy as np

filename = ['aloe.jpg', 'church.jpg' ,'house.jpg' ,'kitchen.jpg']

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
    Cmax = max(r,g,b)
    Cmin = min(r,g,b)
    theta = Cmax - Cmin
    if (theta == 0):
        h = 0
    elif(Cmax == r):
        h = 1/3*math.pi*(((g-b)/theta)%6)
    elif(Cmax == g):
        h = 1/3*math.pi*(((b-r)/theta)+2)
    else:
        h = 1/3*math.pi*(((b-r)/theta)+4)
    if(Cmax == 0):
        s = 0
    else:
        s = theta / Cmax
    v = Cmax
    return round(255*h),round(255*s),round(255*v)
def hsitorgb(h, s, v):
    h = h / 255
    s = s / 255
    v = v / 255
    #h = h / 180 * math.pi
    C = s * v
    X = C*(1 - abs((h / 1/3*math.pi)%2 -1))
    m = v - C
    if(h < 1/3*math.pi and h >= 0):
        r,g,b = C,X,0
    elif(h < 2/3*math.pi and h >= 1/3*math.pi):
        r,g,b = X,C,0
    elif(h < math.pi and h >= 2/3*math.pi):
        r,g,b = 0,C,X
    elif(h < 4/3*math.pi and h >= math.pi):
        r,g,b = 0,X,C
    elif(h < 5/3*math.pi and h >= 4/3*math.pi):
        r,g,b = X,0,C
    else:
        r,g,b = C,0,X
    return round((r+m)*255) ,round((g+m)*255) ,round((b+m)*255)
for i in filename:
    img = Image.open(i).convert("RGB")
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
    h_list = []
    s_list = []
    i_list = []
    for i in range(row):
        for j in range(col):
                h_list.append(pixel[i,j][0])
                s_list.append(pixel[i,j][1])
                i_list.append(pixel[i,j][2])
    array = np.array(i_list)
    #i_list = hiseq(array,row,col)
    for i in range(row):
        for j in range(col):
            img2.putpixel((i , j),(h_list[i * col + j], s_list[i * col + j], i_list[i * col + j]) )
    for i in range(row):
        for j in range(col):
            h, s, v = img2.getpixel((i, j))
            (r, g, b) = hsitorgb(h, s, v)
            img2.putpixel((i,j) , (r, g, b))
    img2.show()