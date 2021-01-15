


from utils.deal_before import deal_before_2
from utils.get_info import get_rgb
from utils.palette import k_means


def Photo_GetColor_By_k(img_name,k_palette):

    #多一位黑色
    img_lab, n_pixels, n_channels = deal_before_2(img_name);
    centers,labels = k_means(img_lab,k_palette,init_mean=True)
    colors_rgb = get_rgb(centers, labels, n_channels, k_palette);

    return colors_rgb
