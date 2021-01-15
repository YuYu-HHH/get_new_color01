import time

import numpy as np
from get_score import *
from utils.rgblab import rgb2lab
from utils.rgblab import *
import multiprocessing

from get_score.get_scores import get_score


def cal(color_use_,count,score):
    score_1 = 0;
    t1 = time.time();
    return_score = [];
    return_color = [];
    color1 = np.linspace(0, 255, 6);
    for i in range(len(color1)):
        for j in range(len(color1)):
            for k in range(len(color1)):
                color_use_1 = np.transpose(color_use_)
                column_use = [color1[i], color1[j], color1[k]];
                column_use = np.array(column_use);
                color_use_1[count] = column_use;
                color_use_1 = np.transpose(color_use_1);
                score_use = get_score(color_use_1);
                if score_use > score_1:
                    score_1 = score_use;
                    column_1 = column_use;


    t2 = time.time();
    color_best_1_lab = rgb2lab(column_1);
    lab_1 = color_best_1_lab[0];
    lab_2 = color_best_1_lab[1];
    lab_3 = color_best_1_lab[2];
    lab_mm_count = 20;
    lab_1_min = lab_1 - lab_mm_count;
    lab_1_max = lab_1 + lab_mm_count;
    lab_2_min = lab_2 - lab_mm_count;
    lab_2_max = lab_2 + lab_mm_count;
    lab_3_min = lab_3 - lab_mm_count;
    lab_3_max = lab_3 + lab_mm_count;
    for i in np.arange(lab_1_min, lab_1_max, 20):
        for j in np.arange(lab_2_min, lab_2_max, 20):
            for k in np.arange(lab_3_min, lab_3_max, 20):
                lab_use = np.array([i, j, k]);
                rgb_use = lab2rgb(lab_use);
                color_2 = np.transpose(color_use_);
                color_2[count] = rgb_use;
                color_2 = np.transpose(color_2);
                score_2_use = get_score(color_2);
                if score_2_use > score + 0.1:
                    score_2 = score_2_use;
                    color_2 = color_2;
                    return_score.append(score_2);
                    return_color.append(color_2);
    return return_color,return_score;

def get_better_color_by_cal_3(color,score):

    color_use_ = color;
    x = len(color[0]);


    msgs = [];
    for count in range(x):
        msgs.append([color_use_,count,score]);
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        return_inf = pool.starmap(cal, msgs)
    colors = [];
    scores = [];
    for i in range(x):
        if return_inf[i][1] != []:
            colors.append(return_inf[i][0]);
            scores.append(return_inf[i][1]);
    return_colors = [];
    return_scores = [];
    if color[0] == []:
        return_info = 0;
    else:
        return_info = 1;
        for o in range(len(scores)):
            return_colors.append(np.array(colors[o][0]));
            return_scores.append(np.array(scores[o][0]));
    return return_colors, return_scores,return_info;
