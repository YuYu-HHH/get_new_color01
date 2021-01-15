from get_color_from_photo.Photo_GetColor_ import Photo_GetColor_
from get_color_from_photo.Photo_Recoloring_do import Photo_GetColor_By_k
from utils.deal_before import get_n_pixels


def get_colors_fromphoto(img_filename):
    k_palette = 10;
    n_pixels = get_n_pixels(img_filename)
    if n_pixels < 5000:
        colors_rgb = Photo_GetColor_(img_filename, 0);
    else:
        colors_rgb = Photo_GetColor_By_k(img_filename, k_palette);
    return colors_rgb;