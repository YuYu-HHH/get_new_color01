from get_new_color import get_new_color


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    dir = 'D:/pycharmFilePicture/picture1/'
    res_dir = "D:/pycharmFilePicture/picture_res/"
    number = 1;
    # number = 2;
    get_new_color(dir,res_dir,number);


if __name__ == '__main__':

    print_hi('get_new_color')
