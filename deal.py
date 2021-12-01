import os
import cv2
import numpy as np
def walkPictures(rootPath):
    for root, dirs, files in os.walk(rootPath):
        for d1 in dirs:
            for root1, dirs1, files1 in os.walk(os.path.join(rootPath, d1)):
                for file in files1:
                    path2 = os.path.join(os.path.join(rootPath, d1), file)
                    im = cv2.imdecode(np.fromfile(path2, dtype=np.uint8), cv2.IMREAD_COLOR)
                    # 原始图像大小
                    (h, w) = im.shape[:2]

                    # 目标大小
                    dst_size = (512,512)

                    # 使用最近邻插值法
                    method = cv2.INTER_NEAREST

                    # 缩放
                    im = cv2.resize(im, dst_size, interpolation = method)

                    cv2.imencode('.jpg',im)[1].tofile(path2)

            print(os.path.join(rootPath, d1))

def main():
    walkPictures("D:\学校杂项\数据采集任务\数据集制作\白吉康 - 副本")

if __name__ == '__main__':
    main()