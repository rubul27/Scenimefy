# General Video-to-Anime Translation with Scenimefy

Transforming real-world videos into anime-style videos by training **Scenimefy** (ICCV 2023), a
semi-supervised image-to-image translation framework, and applying it frame by frame.

**Course project:** Deep Learning: Theory and Practice (IE-643), IIT Bombay, under Prof. P. Balamurugan · Aug–Nov 2024
**Team Projectneo:** Rubul Gogoi, Amitkumar Kumavat

> Built on the official Scenimefy implementation: *Scenimefy: Learning to Craft Anime Scene via
> Semi-Supervised Image-to-Image Translation*, Jiang, Jiang, Yang & Loy (ICCV 2023) ·
> [paper](https://arxiv.org/abs/2308.12968) · [code](https://github.com/Yuxinn-J/Scenimefy).
> All credit for the method goes to the original authors.

## What we did

- **Explored baselines** for image-to-anime translation (pix2pix, CycleGAN, CartoonGAN, AnimeGAN) and
  attempted a custom GAN before selecting Scenimefy.
- **Collected anime data:** extracted 5,958 Shinkai-style scene frames from nine films using the
  frame list provided with Scenimefy.
- **Trained Scenimefy's unsupervised translation branch from scratch** using the official codebase,
  and added checkpoint resumption.
- **Implemented FID evaluation** and compared training-data sizes.
- **Extended image translation to video:** frame extraction → per-frame anime translation → video reconstruction.

## Method

Scenimefy is a semi-supervised framework with three stages: pseudo-paired data generation,
segmentation-guided data selection, and semi-supervised translation with a supervised branch
(on pseudo pairs) and an unsupervised branch (on unpaired real/anime images).

**This project trains the unsupervised branch only.** It learns real → anime translation from
unpaired images, based on Contrastive Unpaired Translation (CUT), with:
- **Adversarial (GAN) loss:** a discriminator compares generated images with real Shinkai frames.
- **Semantic Relation Consistency (SRC) loss:** keeps relations between image patches
  (e.g. sky, mountain, sea) consistent between the input and the stylized output.
- **Hard-negative contrastive (hDCE) loss:** a patch-wise contrastive loss with harder negatives,
  so the stylized output stays faithful to the input's content.

The supervised branch (pseudo-paired data with the StylePatchNCE loss) was not used.

## Data

| Dataset | Size | Use |
|---------|------|-----|
| LHQ (real landscapes) | 30,000 images | source domain (`unpaired_s2a/trainA`) |
| Shinkai anime scenes | 5,958 images | target domain (`unpaired_s2a/trainB`) |

## Training setup

- Base: CUT; generator `resnet_9blocks`; 70×70 PatchGAN discriminator; `mlp_sample` feature head
- Batch size 1, image size 704×704, NCE layers 0, 4, 8, 12, 16, instance normalization
- Loss weights: GAN = 1, hDCE = 1, SRC = 1
- Adam (β1 = 0.5, β2 = 0.999), lr 2e-4 constant for 10 epochs, then linear decay to 0 over 10 epochs

## Results

Both runs use the same Shinkai-style anime domain and the unsupervised branch; only the amount of
anime training data changes.

| Run | Anime images | FID ↓ |
|-----|--------------|-------|
| Small data | 1,357 | 361.29 |
| **Full data** | **5,958** | **58.10** |

Increasing the anime images ~4.4× reduced FID from 361 to 58. Without paired supervision, the
model relies entirely on the discriminator learning the anime style from real anime frames, so the
amount of anime data matters a great deal.

*Note: the presentation labels the first run "SummerWar"; it used a smaller Shinkai-style subset.*
