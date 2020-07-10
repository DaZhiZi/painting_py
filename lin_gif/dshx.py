from utils import (
    log,
    random_num,
    floor,
    formatted_image,
    text,
)
from PIL import Image
import os
import imageio

def get_imgs():
    path = 'C:\\Users\\lichao\\Desktop\\lin_gif'
    pathname = path + '\\new_img'
    l = []
    for root, dirs, names in os.walk(path):
        for filename in names:
            name = filename.split('.')[1]

            # log('name', name)
            if name == 'png':
                # log('filename', filename, 'root', root)
                filename = os.path.join(pathname, filename)
                l.append(filename)
    # log('l', l)
    return l
    pass


def dshx():
    # image_list = []

    filenames = get_imgs()
    images = []
    for filename in filenames:
        log('filename', filename)
        images.append(imageio.imread(filename))
    imageio.mimsave('my.gif', images, duration=0.8)
    # img = Image.open(imgs[0])
    # for i in range(len(imgs)):
    #     log('imgs[i]', imgs[i], i)
    #     path = imgs[i]
    #     img = Image.open(path)
    #     image_list.append(img)
    #
    # list_path = 'C:\\Users\\lichao\\Desktop\\dshx.gif'
    # # duration 指的是动图每两张之间的时间间隔，其他的设置我是照抄的
    # img.save(list_path, save_all=True, append_images=image_list, duration=1000)


def main():
    dshx()
    # get_imgs()
    pass


if __name__ == '__main__':
    main()
