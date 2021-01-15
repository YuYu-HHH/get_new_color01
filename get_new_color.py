from get_score_allpictures_2 import get_score_allpicture_2
from utils.judge_dir import judge_dir
import time

def get_new_color(dir,res_dir):
    res = judge_dir(dir, res_dir);
    if res == 1:
        t1 = time.time()

        get_score_allpicture_2(dir, res_dir);

        t2 = time.time();
        print('Total time: {}'.format(str(t2 - t1)))
    else:
        print("请检查文件夹")