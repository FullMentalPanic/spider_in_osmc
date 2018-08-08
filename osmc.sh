#!/bin/bash
sudo mount /dev/sda1 /home/osmc/hdd/
source /home/osmc/script/env/bin/activate
cd /home/osmc/script/PiSpider/
pwd
python3 main.py
