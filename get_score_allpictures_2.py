import multiprocessing
import os
import time
from os import listdir
from os.path import join
import numpy as np

from cal_new_color.get_better_color_by_cal import get_better_color_by_cal
from cal_new_color.get_better_color_by_cal_3 import get_better_color_by_cal_3
from get_color_from_photo.get_colors_fromphoto import get_colors_fromphoto
from get_score.get_scores import get_score
from transfer_photo.transfer_photo import transfer_photo
from utils.get_info import get_lab_info
from utils.judge_dir import get_filenames
from utils.sorted_color import save_picture_1, save_picture_2


# 获取图片的颜色,输出图片的rgb
# 获取颜色的得分,计算前五颜色的得分
# 得到更高得分的颜色组合
# 重新上色
def get_score_allpicture_2(dir,res_dir,number):
    # 获取文件夹里面的图片，和图片的名称
    fileNames , img_filenames = get_filenames(dir);
    # 文件夹中图片的数量
    img_filename_shape = len(np.array(img_filenames));
    print("一共有{}张图片".format(img_filename_shape));
    for i in range(img_filename_shape):

        t1 = time.time()
        colors_rgb = get_colors_fromphoto(img_filenames[i])
        t2 = time.time();
        print('Photo_GetColor_By_k的运行时间: {}'.format(str(t2 - t1)))

        colors_res = np.array(colors_rgb);
        color_1 = np.transpose(colors_res);
        # colors_lab = get_lab_info(colors_res);
        if len(color_1[0]) < 5:
            print(len(color_1[0]))
            print('颜色太少了');
            break;
        else:
            t = 5;

        color_1 = color_1[:, 0:t];
        color_1 = list(color_1);
        colors_res = colors_res[0:t,:];
        colors_lab = get_lab_info(colors_res);
        save_picture_1(np.transpose(color_1), fileNames[i],number);
        # 得到更好得分的颜色组合,转换颜色
        score_1 = get_score(color_1);
        t3 = time.time();
        if number == 2:
            color_2s, score_2s, info = get_better_color_by_cal(color_1, score_1);
            t4 = time.time();
            print('get_better_color_by_cal的运行时间: {}'.format(str(t4 - t3)));
        else:
            if number == 1:
                color_2s,score_2s,info = get_better_color_by_cal_3(color_1,score_1);
                t4 = time.time();
                print('get_better_color_by_cal_3的运行时间: {}'.format(str(t4 - t3)));


        ori_RGB = str(np.array(color_1))
        res_RGB = str(color_2s)
        ori_LAB = str(colors_lab)
        res_score_2s = str(score_2s)
        if not os.path.exists('./res_info/'):
            os.mkdir('./res_info/');
        dir_res_info = './res_info/' + fileNames[i];
        if not os.path.exists(dir_res_info):
            os.mkdir(dir_res_info);
        with open(dir_res_info + '/结果存放picture.txt', 'a') as file_handle:
            file_handle.write(fileNames[i] )
            file_handle.write('\n')
            file_handle.write( "ori_RGB")
            file_handle.write('\n')
            file_handle.write(ori_RGB)
            file_handle.write('\n')
            file_handle.write("res_score_2s")
            file_handle.write('\n')
            file_handle.write(res_score_2s)
            file_handle.write('\n')
            file_handle.write("res_RGB")
            file_handle.write('\n')
            file_handle.write(res_RGB)
            file_handle.write('\n')
            file_handle.write('ori_LAB')
            file_handle.write('\n')
            file_handle.write(ori_LAB)
            file_handle.write('\n')


        if info == 1:
            t5 = time.time();
            msgs = [];
            colors_lab = np.array(colors_lab);
            colors_lab = colors_lab[0:t, :];
            print(colors_lab)
            for j in range(len(score_2s)):

                color_2 = color_2s[j];
                color_2 = np.transpose(color_2);
                lab_color = get_lab_info(color_2);
                save_picture_2(color_2, fileNames[i], j,number);
                # print(lab_color)
                lab_color = lab_color[0:t, :];
                # print(lab_color)
                msgs.append([img_filenames[i],fileNames[i],colors_lab,lab_color,j,dir,res_dir,number]);
                res_LAB = str(lab_color)
                with open(dir_res_info + '/结果存放picture.txt', 'a') as file_handle:
                    file_handle.write('res_LAB      :::' + str(j))
                    file_handle.write('\n')
                    file_handle.write(res_LAB)
                    file_handle.write('\n')

            with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
                pool.starmap(transfer_photo, msgs);
            t6 = time.time();
            print('transfer_photo的运行时间: {}'.format(str(t6 - t5)));







