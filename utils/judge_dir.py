import os
import os
import time
from os import listdir
from os.path import join

#判断文件夹是否存在
def judge_dir(dir,res_dir):
    if not os.path.exists(dir):
        print("文件夹不存在")
    else:
        if not os.path.exists(res_dir):
            os.mkdir(res_dir)
            return 1;
        else:
            return 1;


def isornot_image(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def get_filenames(dir):
    img_filenames = [];
    fileNames = [];
    for x in listdir(dir):
        if isornot_image(x):
            img_filename = join(dir, x);
            img_filenames.append(img_filename);
            fileName = os.path.splitext(x)[0]
            fileNames.append(fileName)

    return fileNames,img_filenames;

