from PIL import Image
import math


def rgbtohsi(R, G, B):
    r = R / 255
    g = G / 255
    b = B / 255
    num = 0.5 * ((r - g) + (r - b))
    den = ((r - g) * (r - g) + (r - b) * (g - b)) ** (0.5)
    if (b <= g):

        if den != 0:
            h = math.acos(num / (den))  # h value
        else:
            h = 0
    elif (b > g):
        if den != 0:
            h = (2 * math.pi) - math.acos(num / den)  # h value
        else:
            h = 0
    if(r + g + b == 0):
        s=0
    else:
        s = 1 - (3 * min(r, g, b) / (r + g + b))  # s value
    i = (r + g + b) / 3  # i value
    return int(h * 180 / math.pi), int(s * 100), int(i * 255)
img = Image.open("aloe.jpg").convert("RGB")
img1 = img.copy()
pixel = img1.load()
row = img1.size[0]
col = img1.size[1]
for i in range(row):
    for j in range(col):
        r, g, b = img1.getpixel([i, j])
        h, s, v = rgbtohsi(r, g, b)
        pixel[i, j] = [h, s, v]
#img.show()
print()
img1.show()