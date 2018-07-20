# -*- coding: utf-8 -*-
# all linux cmd used in python code
import subprocess
import os

def Add_Torrent(url,location):
    transmission_add_torrent = ['/usr/bin/transmission-remote', "-n", "transmission:transmission",]

    transmission_add_torrent.append("--add")
    transmission_add_torrent.append(url)
    transmission_add_torrent.append("-w")
    transmission_add_torrent.append(location)
    return subprocess.call(transmission_add_torrent)

def List_Torrent():
    transmission_list = ["/usr/bin/transmission-remote -n transmission:transmission -l"]
    temp, err = subprocess.Popen(transmission_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True).communicate()
    var = []
    temp = str(temp)
    for line in temp.split('\\n'):
        print (line)
        var.append(line)
    var.pop(-1)
    var.pop(-1)
    var.pop(0)
    return var

def Start_Transmission():
    transmission_start = ['sudo', 'service', 'transmission-daemon', 'start']
    subprocess.call(transmission_start)

def Stop_Transmission():
    transmission_stop = ['sudo', 'service', 'transmission-daemon', 'stop']
    subprocess.call(transmission_stop)

def Run_Spider():
    scrapy = ['scrapy', 'crawl', 'dmhy_rss']
    var = subprocess.check_output(scrapy)

def Romove_Torrent(id):
    transmission_remove = ['/usr/bin/transmission-remote', "-n", "transmission:transmission",]
    temp = str(id)
    transmission_remove.append(temp)
    temp = '-r'
    transmission_remove.append(temp)
    subprocess.call(transmission_remove)

def remove_transmission_finish_work():
    check_list =  List_Torrent()
    if not check_list:
        pass
    else:
        ID ='-t'
        for item in check_list:
            temp = item.split()
            if temp[4] == 'Done':
                ID = ID+temp[0]+','
            else:
                pass
        if ID != '-t':
            Romove_Torrent(ID)
        else:
            pass