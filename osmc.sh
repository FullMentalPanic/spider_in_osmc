#!/bin/bash
sleep 10s
sudo mount /dev/sda1 /home/osmc/hdd/
sudo service transmission-daemon start
source /home/osmc/script/env/bin/activate
cd /home/osmc/script/PiSpider/
pwd
sudo python3 main.py
