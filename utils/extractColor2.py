from PIL import Image, ImageCms
import math

from utils.get_info import get_rgb
from utils.sorted_color import save_picture_1


def rgb2lab(image):
	RGB_p = ImageCms.createProfile('sRGB')
	LAB_p = ImageCms.createProfile('LAB')
	return ImageCms.profileToProfile(image, RGB_p, LAB_p, outputMode='LAB')

def lab2rgb(image):
	RGB_p = ImageCms.createProfile('sRGB')
	LAB_p = ImageCms.createProfile('LAB')
	return ImageCms.profileToProfile(image, LAB_p, RGB_p, outputMode='RGB')

def extractColor2(sourceImg, color_cnt):
    img = Image.open(sourceImg)
    # print(img.format, img.size, img.mode)
    lab = rgb2lab(img)
    colors = lab.getcolors(img.width * img.height)
    bins = {}
    smallarea = img.width * img.height / 7000
    for count, pixel in colors:
        if count <= smallarea:
            continue
        bins[pixel] = count
    bins =  {k: v for k, v in sorted(bins.items(), key=lambda item: item[1], reverse=True)}
    bins = list(bins.keys())
    #print(bins[:20])
    if len(bins) <= color_cnt:
        a = [bins[-1]]*(color_cnt-len(bins))
        bins.extend(a)
        return bins
    elif len(bins) > 10*color_cnt:
        bins = bins[:10*color_cnt]
    L, a, b = 0, 1, 2
    bindis = {}
    for i in range(len(bins)):
        for j in range(i+1, len(bins)):
            #L1, L2 = bins[i][L], bins[j][L]
            a1, a2 = bins[i][a], bins[j][a]
            b1, b2 = bins[i][b], bins[j][b]
            bindis[(i, j)] = math.sqrt((a1-a2)**2 + (b1-b2)**2)
    bindis =  {k: v for k, v in sorted(bindis.items(), key=lambda item: item[1])}
    bindisKeys = list(bindis.keys())
    removeIndexes = []
    n = len(bins) - color_cnt
    print(len(bins))
    for i in range(n):
        jk = bindisKeys[0]
        removeIndexes.append(jk[1])
        #bins[jk[0]] = ((bins[jk[0]][0] + bins[jk[1]][0])/2, (bins[jk[0]][1] + bins[jk[1]][1])/2, (bins[jk[0]][2] + bins[jk[1]][2])/2)
        bindisKeys2 = []
        for key in bindisKeys:
            if jk[1] not in key:
                bindisKeys2.append(key)
        bindisKeys = bindisKeys2
    colors = []
    for i in range(len(bins)):
        if i not in removeIndexes:
            colors.append(bins[i])

    return colors

