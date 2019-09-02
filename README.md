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


## Usage
```
├── dataset
  └── YOUR_DATASET_NAME
    ├── images
      ├── training
        ├── 000001.jpg
        ├── 000002.png
        └── ...
      ├── validation
        ├── 000001.jpg
        ├── 000002.png
        └── ...
    ├── annotations
      ├── training
        ├── 000001.jpg
        ├── 000002.png
        └── ...
      ├── validation
        ├── 000001.jpg
        ├── 000002.png
        └── ...
0.jpg (example for guided image translation task)

```

**CelebAMask-HQ**
* Download from [here](https://github.com/switchablenorms/CelebAMask-HQ)
You could use celebmask.py to handle the dataset.


## result

<table align='center'>
<tr align='center'>
<td> </td>
<td> traditional conditional GANs </td>
<td> acGANs </td>
</tr>
<tr align='center'>
<td></td>
<td><img src = 'result/2_20.png' height = '300px'>
<td><img src = 'result/MNIST_ACGAN_30.png' height = '300px'>
</tr>
</table>
<tr align='center'>
<td></td>
    guided image generation
<td><img src = 'result/women_guide_hinge.png' height = '300px'>
    random image generation
<td><img src = 'result/women_random_hinge.png' height = '300px'>
</tr>






