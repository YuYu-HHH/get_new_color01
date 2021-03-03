


from utils.deal_before import deal_before_2
from utils.extractColor2 import extractColor2
from utils.get_info import get_rgb, get_rgb_1
from utils.palette import k_means


def Photo_GetColor_By_k(img_name,k_palette):

    #多一位黑色
    img_lab, n_pixels, n_channels = deal_before_2(img_name);
    # centers,labels = k_means(img_lab,k_palette,init_mean=True)
    # colors_rgb = get_rgb(centers, labels, n_channels, k_palette);
    centers = extractColor2(img_name, 5)
    colors_rgb = get_rgb_1(centers, n_channels, 5);
    return colors_rgb
