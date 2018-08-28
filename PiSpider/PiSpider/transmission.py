# -*- coding: utf-8 -*-
# all linux cmd used in python code
import subprocess
import os
import transmissionrpc
import time

class Transmission_control(object):
    def __init__(self):
        count = 0
        self.tc = None
        while count <3:
            try:
                self.tc = transmissionrpc.Client('localhost', port=9091, user = 'transmission', password = 'transmission')
            except transmissionrpc.error.TransmissionError:
                time.sleep(60)
                count = count + 1
            else:
                break
        if count >=3:
            raise Exception("time out")

    def download_torrent(self, torrent, location):
        base_path = "/home/osmc/hdd/download/"
        abs_path = base_path + str(location)+'/'
        if not os.path.isdir(abs_path):
            self.creat_folder(abs_path)
        self.tc.add_torrent(torrent,download_dir=abs_path)

    def creat_folder(self, dir):
        subprocess.call(['mkdir',dir])
        subprocess.call(['sudo','chmod', '-R', '777', dir])

    def remove_finish_torrent(self):
        for torrent in self.tc.get_torrents():
            if torrent.isFinished is True:
                self.tc.remove_torrent(torrent.id)
            else:
                pass

    def close(self):
        self.tc = None
