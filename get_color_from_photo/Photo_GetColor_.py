from get_color_from_photo.GetColor import get_Color
from utils.deal_before import deal_before_
from utils.get_info import get_rgb


def Photo_GetColor_(img_name,d):


    img_lab,colors,n_pixels,n_channels = deal_before_(img_name);
    if n_pixels < 3000:
        d = 0.0000001;
    else:
        d = 0.3;
    centers,new_centers,labels,k_palette1 = get_Color(img_lab,n_pixels,n_channels,d);

    colors_rgb = get_rgb(centers,labels,n_channels,k_palette1);

    return colors_rgb
