docker run -it --gpus all -v /home/kasuich/projects/summer_school_project/demo/summer_school_project:/workspace/ -v /home/kasuich/.cache/:/home/user/.cache/ -p 7007:7007 -p 8501:8501 --rm --ipc=host 3d-reconstruction
