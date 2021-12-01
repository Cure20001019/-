import os
import argparse

def rename_image(src_dir, date, name):
    i = 0
    sub_dirs = os.listdir(src_dir)
    for sub_dir in sub_dirs:
        if not os.path.isdir(os.path.join(src_dir, sub_dir)):
            print("{} isn't subdir. Skiped it.".format(sub_dir))
            continue
        else:
            num = 1
            for image in os.listdir(os.path.join(src_dir, sub_dir)):
                org_name, ext = image.split(sep=".", maxsplit=1)
                os.rename(os.path.join(src_dir, sub_dir, image), \
                        os.path.join(src_dir, sub_dir, "{}_{}_{:04}.{}".format(date, name, num, ext))) 
                num += 1
            i+=1
        print("{} done".format(sub_dir))
    print("{} folders renamed in total.".format(i))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A batch file-renaming script.')
    parser.add_argument('--date', type=str, metavar='S',
                        help="Shooting time.")
    parser.add_argument('--name', type=str, metavar='S',
                        help="Your name.")
    args = parser.parse_args()

    src_dir = "../../16-崔言杰_edited"

    rename_image(src_dir, args.date, args.name)
