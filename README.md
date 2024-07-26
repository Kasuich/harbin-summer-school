# Harbin Summer School, 2nd Project

This is a report on a 2nd project "Single-image 3D Multiview Reconstruction". 

## Installation Guide

❗ Make sure to enter your username in .env file

```
docker build -t 3d-reconstruction .
bash run.sh
```

GUI Interface will be exposed at 8501 port

## Overview
Era3D, a novel multiview diffusion method that generates high-resolution multiview images from a single-view image.
After studying [this article](https://arxiv.org/pdf/2405.11616), we have highlighted several points about Era3D:

* **Camera positioning**  
Orthogonal cameras and viewpoint on an elevation of 0 degrees. This assumption allows them significantly improve computational complexity and eliminates distortion.
* **Focal length rectification**   
New regression and condition scheme and utilization of the low-level feature maps of UNet at each denoising step to predict camera information.
* **Row-wise multiview attention**  
Row-wise multiview attention that enabled them to decrease computational costs for high-resolution images

## Outcomes
### Done:
 - ✅ Overviewing research of a SOTA approches
 - ✅ Deeper understanding of 3D Reconstruction fundamentals
 - ✅ GUI Interface to get access to the Era3D model
 - ✅ Dockerization of the GUI Interface

### To be continued:
 - ➡️ Model training and inference using Gaussian Splatting 
 - ➡️ Local inference of the model
 - ➡️ Separate the model from the GUI Interface service
 - ➡️ 3D Reconstruction using Gaussian Splatting

### Challenges 🫠:
- 🏋️‍♂️ Lack of available CUDA memory

## Team Members:
- <i>Roman Shinkarenko</i>
- <i>Nikolai Aleksandrov</i>
- <i>Sergey Martynov</i>
- <i>Mariia Ulianova</i>
- <i>Yaroslav Romanenko</i>
