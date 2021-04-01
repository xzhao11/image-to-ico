import os
import PythonMagick
import sys


def convert_single_png(filename, src_pathname, des_pathname):
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        filename = input("Please input a valid image name with extension: ")
        convert_single_png(filename)
    src_image = os.path.join(src_pathname, filename)
    img = PythonMagick.Image(src_image)
    img.sample('256x256')
    ico_name = os.path.splitext(filename)[0] + ".ico"
    des_ico = os.path.join(des_pathname, ico_name)
    img.write(des_ico)
    print("%s --> %s" % (filename, ico_name))


def convert_dir_png(src, des):
    for file in os.listdir(src):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            convert_single_png(file, src, des)


def check_args():
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        print("usage: convert_image_to_ico.py filename/dirname")
        exit(0)


if __name__ == '__main__':
    check_args()
    filename = sys.argv[1]
    if os.path.isfile(filename):
        convert_single_png(filename, "", "")
    elif os.path.isdir(filename):
        des_dir = filename + '-icos'
        if not os.path.exists(filename+'-icos'):
            os.mkdir(filename+'-icos')
        else:
            if len(os.listdir(filename+'-icos')) != 0:
                print("destination folder " + des_dir + " is not empty")
                option = input("Do you want to (a)ppend to the folder? or (m)ake a new folder? ")
                while len(option) == 0 or (option[0].lower() != 'a' and option[0].lower() != 'm'):
                    option = input("please input o for overwrite or m for make a new folder: ")
                option = option[0].lower()
                if option == 'm':
                    des_dir = input("Please input the name for the new folder: ")
                    while len(des_dir) == 0:
                        des_dir = input("Please input a valid name: ")
                    for dir in os.listdir():
                        if os.path.isdir(dir):
                            while dir == des_dir:
                                des_dir = input("Dest folder exits, please input a different name: ")
                    os.mkdir(des_dir)
        convert_dir_png(filename, des_dir)
    else:
        print("usage: convert_image_to_ico.py filename/dirname")
        exit(0)

