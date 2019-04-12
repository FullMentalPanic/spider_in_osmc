#!/bin/bash
git fetch
git checkout -m origin/master PiSpider/PiSpider/config.yml
git add PiSpider/PiSpider/config.yml
git commit
cd /spider_in_osmc/PiSpider/
pwd
python3 main.py
