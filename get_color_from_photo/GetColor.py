from utils import *
import numpy as np

from utils.distance_util import get_Count_By_distance


def get_Color(img_lab,n_pixels,n_channels,d):
    centers = [];
    labels = [];
    centers.append(img_lab[0]);
    labels.append(1)
    j = 0;
    centers_pixels = np.zeros((100, n_pixels+1,n_channels), dtype=int);
    centers_pixels[j][0] = img_lab[0];
    for i in range(1,n_pixels):
        pixel_use = img_lab[i];
        count = get_Count_By_distance(centers,pixel_use,d);
        if count == -1:
            j = j + 1;
            centers.append(pixel_use);
            labels.append(1);
            centers_pixels[j][0] = (pixel_use);
        else:
            centers_pixels[count][labels[count]]= pixel_use;
            labels[count] = labels[count] + 1;
    use = [];

    labels = np.array(labels)
    centers = np.array(centers)


    number = labels.shape[0];

    # 程序没有问题了
    new_centers = np.zeros((number, n_channels), dtype=int);
    for k in range(number):
        centers_1 = np.zeros((number, n_channels), dtype=int);
        centers_pixels_use = centers_pixels[k];
        for p in range(len(centers_pixels_use)):
            for channel_index in range(n_channels):
                centers_1[k][channel_index] = centers_1[k][channel_index] + centers_pixels_use[p][channel_index];

        for channel_index in range(n_channels):
            new_centers[k][channel_index] = centers_1[k][channel_index] / labels[k];

    return centers,new_centers,labels,number;














# def get_Color_2(colors,n_pixels,n_channels,d):
#     # centers = np.zeros((100,n_channels), dtype=int);
#     centers = [];
#     centers_pixels = np.zeros((100,n_channels), dtype=int);
#     labels = np.zeros((100),dtype=int);
#     j = 0;
#     k = 0;
#     labels_use = np.zeros((100), dtype=int);
#     for cnt,pixel in colors:
#         pixel = np.array(pixel);
#         if j == 0:
#             centers.append(pixel);
#             centers_pixels[0] = pixel * cnt;
#             labels[0] = cnt;
#             labels_use[0] = 1;
#             j = j + 1;
#             k = k + 1;
#             print(k)
#         else:
#             count = get_Count_By_distance(centers,pixel,d);
#             if count == -1:
#                 centers.append(pixel);
#                 labels[k] = cnt;
#                 centers_pixels[k] = np.array(pixel )* cnt;
#                 labels_use[k] = 1;
#                 k = k + 1;
#                 print(k)
#             else:
#                 labels[count] = labels[count] + cnt;
#                 labels_use[count] = labels_use[count] + 1;
#                 centers_pixels[count] = centers_pixels[count] + np.array(pixel ) * cnt ;
#     centers = np.array(centers);
#     number = centers.shape[0];
#     new_centers = np.zeros((number, n_channels), dtype=int);
#     for i in range(number):
#         for j in range(n_channels):
#             new_centers[i][j] = centers_pixels[i][j] / labels[i];
#     return centers,new_centers,labels,number;
#
#
#
#
#
#
#
#
#
#
#
#
#
