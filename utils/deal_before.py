
from PIL import Image
import cv2
import numpy as np

#获取图片的基本信息
from utils.palette import sample_bins
from utils.util import rgb2lab


def deal_before_(img_name):
    img = Image.open(img_name);

    img_use = cv2.imread(img_name);

    lab = rgb2lab(img)

    img_lab_use = lab.load();
    img_lab = [];
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            img_lab.append(img_lab_use[i, j]);

    n_pixels = img.width * img.height;
    n_channels = img_use.shape[2];
    colors = lab.getcolors(img.width * img.height);
    img_lab = np.array(img_lab);
    img_lab = img_lab.reshape(n_pixels, n_channels);

    return img_lab,colors,n_pixels,n_channels;
def deal_before_2(img_name):

    img = Image.open(img_name)

    n_pixels = img.width * img.height;

    img_use = cv2.imread(img_name);
    n_channels = img_use.shape[2];
    lab = rgb2lab(img)
    colors = lab.getcolors(img.width * img.height)
    bins = {}
    for count, pixel in colors:
        bins[pixel] = count
    bins = sample_bins(bins)

    return bins,n_pixels,n_channels

def get_n_pixels(img_name):
    img = Image.open(img_name);
    n_pixels = img.width * img.height;
    return n_pixels;