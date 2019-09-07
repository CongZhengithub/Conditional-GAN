import cv2
import os
import numpy as np
mask_dir=os.listdir('CelebAMask-HQ-mask-anno')
mask_dir=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
attributes=['hair', 'l_brow', 'l_eye', 'l_lip', 'mouth', 'neck', 'nose', 'r_brow', 'r_eye', 'skin', 'u_lip', 'cloth', 'l_ear', 'r_ear', 'ear_r', 'hat', 'neck_l', 'eye_g']
for dir in mask_dir:
    image_files=os.listdir(os.path.join('CelebAMask-HQ-mask-anno',dir))
    path=os.path.join('CelebAMask-HQ-mask-anno',dir)
    for i in range(int(dir)*2000,int(dir)*2000+2000):
        result=np.zeros([512,512,3])
        x=20
        for attribute in attributes:
            image_file=os.path.join(path,str(i).zfill(5)+'_'+attribute+'.png')
            x=x+3
            if os.path.exists(image_file):
                result+=cv2.imread(image_file)//255*x
        print(image_file)
        cv2.imwrite(os.path.join('CelebAMask',str(i))+'.png',result)

