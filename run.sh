#!/bin/bash

if [ -f .env ]; then
    export $(cat .env | xargs)
fi

docker run -it --gpus all -v summer_school_project:/workspace/ -v /home/$USERNAME/.cache/:/home/user/.cache/ -p 7007:7007 -p 8501:8501 --rm --ipc=host 3d-reconstruction