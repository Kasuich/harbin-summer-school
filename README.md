# Harbin Summer School, 2nd Project

This is a report on a 2nd project "Single-image 3D Multiview Reconstruction". 

## Installation Guide

Make sure to enter your username inside run.sh

```
docker run -it --gpus all -v summer_school_project:/workspace/ -v /home/<YOUR-USERNAME>/.cache/:/home/user/.cache/ -p 7007:7007 -p 8501:8501 --rm --ipc=host 3d-reconstruction
```

```
docker build -t 3d-reconstruction .
bash run.sh
```

GUI Interface will be exposed at 8501 port

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
- <i>Nikolay Aleksandrov</i>
- <i>Mariia Ulianova</i>
- <i>Yaroslav Romanenko</i>