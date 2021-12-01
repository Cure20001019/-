import os
import shutil

def move_image(src_dir, dst_dir):
    sub_dirs = os.listdir(src_dir)
    for sub_dir in sub_dirs:
        if not os.path.isdir(os.path.join(dst_dir, sub_dir)):
            print("{} doesn't existed. Skiped it.".format(os.path.join(dst_dir, sub_dir)))
            continue
        else:
            for image in os.listdir(os.path.join(src_dir, sub_dir)):
                shutil.move(os.path.join(src_dir, sub_dir, image), os.path.join(dst_dir, sub_dir, image))
        print("{} moved".format(sub_dir))


if __name__ == "__main__":
    # 源目录
    src_dir = "/media/linux/000A9A85000F5E96/17-陈世存_edited"
    # 移动目标目录
    dst_dir = "/media/linux/000A9A85000F5E96/Datasets/BJUT_Dataset/val"

    assert os.path.isdir(src_dir) and os.path.isdir(dst_dir)

    move_image(src_dir, dst_dir)
