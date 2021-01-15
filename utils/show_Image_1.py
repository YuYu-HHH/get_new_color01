
from PIL import Image
import random
import time
import cv2
import numpy as np

from utils.sorted_color import sorted_color
from utils.util import lab2rgb


def get_res(color_count, k):
    res = [];
    for i in range(k):
        for color in color_count:
            color = color.tolist();
            if color not in res:
                res.append(color);
                break
    return res
def get_color_2(color_matrix,k):
    res = [];
    for i in range(k):
        for color in color_matrix[:,i]:
            color = color.tolist();
            if color not in res:
                res.append(color);
                break;
    print(res)
    return res
def get_color_3(color_matrix,k):
    res = [];
    print(color_matrix)
    print(color_matrix.shape)
    print("-----------------------------")
    for i in range(k,k+80*k,80):
        for color in color_matrix:
            color = color.tolist();
            if color not in res:
                res.append(color);
                break
    print(res)
    return res
