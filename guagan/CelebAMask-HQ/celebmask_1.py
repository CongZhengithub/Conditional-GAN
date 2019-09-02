import cv2
import os
import numpy as np
mask_dir=os.listdir('result')
mask_dir=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
attributes=['hair', 'l_brow', 'l_eye', 'l_lip', 'mouth', 'neck', 'nose', 'r_brow', 'r_eye', 'skin', 'u_lip', 'cloth', 'l_ear', 'r_ear', 'ear_r', 'hat', 'neck_l', 'eye_g']
#30，40，50，60，70，80，90，100，110，120，130，140，150，160，170，180，190，200
for dir in mask_dir:
    image_files=os.listdir(os.path.join('result',dir))
    path=os.path.join('result',dir)
    for i in range(int(dir)*2000,int(dir)*2000+2000):
        result=np.zeros([512,512,3])
        x=20
        for attribute in attributes:
            image_file=os.path.join(path,str(i).zfill(5)+'_'+attribute+'.png')
            x=x+3
            if os.path.exists(image_file):
                result+=cv2.imread(image_file)//255*x
        xx=[]
        for ii in range(512):
            for j in range(512):
                for k in range(3):
                    if result[ii,j,k] not in xx:
                        xx.append(result[ii,j,k])
        print(image_file)
        print(xx)
        cv2.imwrite(os.path.join(str(i))+'.png',result)
        break
    break

