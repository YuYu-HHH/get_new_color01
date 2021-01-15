import math

# 计算像素点属于哪个中心点
from utils.util import distance


def attenuation(color, last_mean):
    return 1 - math.exp(((distance(color, last_mean) / 80) ** 2) * -1)
def get_Count_By_distance(centers, pixel_use,d):

    # d_min设置过低会产生多的中心点,许多很相似但是没有归到一类中
    # d_min设置过高产生少的中心点,不相似的归到一类中
    d_min = 1;
    d_b = d;
    count_use = 0;
    for i in range(len(centers)):

        d = attenuation(centers[i], pixel_use);
        if d < d_min:
            d_min = d;
            count_use = i;

    if d_min < d_b:
        count = count_use;
    else:
        count = -1;
    return count;

