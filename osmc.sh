#!/bin/bash
#run scrapy every 4h
source /home/osmc/script/env/bin/activate
cd /home/osmc/script/PiSpider/
pwd
watch -n 432000 python3 main.py
