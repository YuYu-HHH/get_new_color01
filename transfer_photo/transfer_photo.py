import os
import shutil
import time

from PIL import Image

from transfer_photo.transfer1 import sample_RGB_color, img_color_transfer, rbf_weights
from utils.util import rgb2lab


def transfer_photo(img_name,filename,means,means_,i,dir,res_dir):
    img = Image.open(img_name)

    # transfer to lab
    lab = rgb2lab(img)
    sample_level = 16
    sample_colors = sample_RGB_color(sample_level)
    sample_weight_map = rbf_weights(means, sample_colors)
    result = img_color_transfer(lab, means, means_, sample_weight_map, sample_colors, sample_level)
    if not os.path.exists(res_dir):
        os.mkdir(res_dir)
    dir1 = res_dir + str(filename) + "/";
    if not os.path.exists(dir1):
        os.mkdir(dir1)
    dir_file = img_name;
    res_dir_file = dir1 + filename + ".jpg"
    shutil.copy(dir_file, res_dir_file);
    i = str(i);
    filename_res = dir1 + filename +'___'+ i + '_res.jpg'
    result.save(filename_res)
