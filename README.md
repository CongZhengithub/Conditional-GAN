# Conditional-GAN-cDCGAN-acGANs-pix2pix-GuaGAN


## Three different methods to direct the image generation process
 - Conditional GANs based on class label (cGANs, acGANs)
 - Conditional GANs based on edge maps (pix2pix)
 - Conditional GANs based on semantic information (Spade)
 
 

## Reference

 - uM. Mirza and S. Osindero. Conditional generative adversarial nets. arXiv preprint arXiv:1411.1784, 2014.
   
 
 - Augustus Odena, Christopher Olah, and Jonathon Shlens. Conditional image synthesis with auxiliary classifier GANs. In ICML, 2017.
   
 - Isola P , Zhu J Y , Zhou T , et al. Image-to-Image Translation with Conditional Adversarial  Networks[J]. CVPR, 2017.
   
 - Park T , Liu M Y , Wang T C , et al. Semantic Image Synthesis with Spatially-Adaptive Normalization[J]. 2019.
   
   
   

## Train
nohup python -u tensorflow_MNIST_cDCGAN_1.py > out_cdcgans.log 2>&1 &

nohup python -u acgan.py > out_acgan.log 2>&1 &

nohup python -u main.py --dataset CelebAMask-HQ  --img_ch 3 --segmap_ch 3 --gpu '1' --phase train > out_1.log 2>&1 &

## random_test for guagan
python main.py --dataset CelebAMask-HQ --segmap_ch 3 --phase random

## Guide test for guagan
python main.py --dataset CelebAMask-HQ --img_ch 3 --segmap_ch 3 --phase guide --guide_img 0.jpg



