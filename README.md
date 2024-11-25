## **Python Script**
Inference! Simply run the following command :
```cd Semi_translation

python test.py --dataroot ./datasets/Sample --name shinkai-test --CUT_mode CUT  --model cut --phase test --epoch Shinkai --preprocess none
```
- * Results will be saved in ./Semi_translation/results/shinkai-test/
- * To prepare our own test images, we have to refer to the data folder structure in ./Semi_translation/datasets/Sample, and place the test images in testA.

## **Quick I2I Train**
### **Dataset Preparation**
- **[LHQ dataset](https://github.com/universome/alis#lhq-dataset)**: a dataset of 90,000 nature landscape images [[downlaod link](https://disk.yandex.ru/d/HPEEntpLv8homg)]. We place it in `./datasets/unpaired_s2a`, and rename as `trainA`.
- **Anime dataset**: 5,958 shinkai-style anime scene images. Please follow the instructions in [`Anime_dataset/README.md`](Anime_dataset/README.md). Place it in `./datasets/unpaired_s2a`, and rename as `trainB`.
- **Pseudo-paired dataset**: 30,000 synthetic pseudo paired images generated from StyleGAN with the same seed. We may finetune your own StyleGAN or use our provided data [[downlaod link](https://entuedu-my.sharepoint.com/:u:/g/personal/c200203_e_ntu_edu_sg/EaZ-8U_3HbBKh9qq4AfJWmUByIuPwn_3GEDpPc84GXuU7w?e=gAs850)] for quick start. Place them in `./datasets/pair_s2a`
- ### Training
Refer to the [`./Semi_translation/script/train.sh`](./Semi_translation/script/train.sh) file, or use the following command:
  ```
  python train.py --name exp_shinkai  --CUT_mode CUT --model semi_cut \ 
  --dataroot ./datasets/unpaired_s2a --paired_dataroot ./datasets/pair_s2a \ 
  --checkpoints_dir ./pretrained_models 
  ```
  - If the anime dataset quality is low, consider add a global perceptual loss to maintain content consistency, e.g., set `--lambda_VGG 0.2`.

- ### Training from checkpoint
 -  Use the following command
   ```
   python trial.py --continue_train --epoch latest_epoch --epoch_count latest_epoch --preprocess resize_and_crop  --name shinkai-test
   ```
### Segmenation Selection
- Follow the instructions in [`Seg_selection/README.md`](Seg_selection/README.md).

  ## :love_you_gesture: Citation

```bibtex
@inproceedings{jiang2023scenimefy,
  title={Scenimefy: Learning to Craft Anime Scene via Semi-Supervised Image-to-Image Translation},
  author={Jiang, Yuxin and Jiang, Liming and Yang, Shuai and Loy, Chen Change},
  booktitle={ICCV},
  year={2023}
}
```
