# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import os
import cv2


# %%
def batch_resize(src_dir, dst_dir, img_size, landmark):
    dst_width  = img_size[0]
    dst_height = img_size[1]

    for img in os.listdir(os.path.join(src_dir, landmark)):
        org_array = cv2.imread(os.path.join(src_dir, landmark, img), cv2.IMREAD_COLOR)
        new_array = cv2.resize(org_array, (dst_width, dst_height), interpolation=cv2.INTER_AREA)
        
        cv2.imwrite(os.path.join(dst_dir, img), new_array)

    print("{} finished.".format(landmark))


# %%
if __name__ == '__main__':
    src_dir = "/media/linux/000A9A85000F5E96/17-陈世存"
    dst_dir = src_dir + "_edited" 
    img_size=[512,512]
    i=0

    if not os.path.exists(dst_dir):
       os.makedirs(dst_dir)
       print("{} created.".format(dst_dir)) 

    for landmark in os.listdir(src_dir):
        if os.path.exists(os.path.join(dst_dir, landmark)):
            print("{} existed.".format(landmark))
            continue
        else:
            save_path = os.path.join(dst_dir, landmark)
            os.mkdir(save_path)
            batch_resize(src_dir, save_path, img_size, landmark)
            i+=1
    print("{:>3d} folders processed in total.".format(i))
