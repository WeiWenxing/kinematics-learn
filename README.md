# Mini Pupper kinematics learn
[MangDang](https://www.mangdang.net/) Online channel: [Discord](https://discord.gg/xJdt3dHBVw), [FaceBook](https://www.facebook.com/groups/716473723088464), [YouTube](https://www.youtube.com/channel/UCqHWYGXmnoO7VWHmENje3ug/featured), [Twitter](https://twitter.com/LeggedRobot)

Mini Pupper will make robotics easier for schools, homeschool families, enthusiasts and beyond.

- Generative AI: Support Google Gemini
- ROS: support ROS2(Humble) SLAM & Navigation robot dog at low-cost price
- OpenCV: support OpenCV official OAK-D-Lite 3D camera module and MIPI camera
- Open-source: DIY and customize what you want.
- Raspberry Pi: it’s super expandable, endorsed by Raspberry Pi.

## Overview

This repository is kinematics learning, it can be run on Mini Pupper. 
The new branch for Mini Pupper2 will be added soon.

## Preparation

Please make sure Mini Pupper can walk first. 

Step 1: Install the [BSP repo](https://github.com/mangdangroboticsclub/mini_pupper_bsp)

Step 2: Install the [quadruped repo](https://github.com/mangdangroboticsclub/StanfordQuadruped )


## Run on Mini Pupper: 

[![Installation Guide]

1. Startup Server on Mini Pupper, clone this repo.
```
cd ~
git clone https://github.com/WeiWenxing/kinematics-learn
cd kinematics-learn
python JupyterServer.py 
```
If error occur about permission, you can add sudo, like:
```
sudo python JupyterServer.py
```

2. Start Jupyter on your PC:
```
git clone https://github.com/WeiWenxing/kinematics-learn
cd kinematics-learn
python -m jupyter jupyternb
```

And then, on your PC, edit Kinematics_learn.ipynb, find "HOST = '192.168.1.105'\n", change the ip address to your pupper's ip address.

Run Kinematics_learn.ipynb on your PC jupyter lab

