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
                self.tc = transmissionrpc.Client('192.168.1.101', port=9091, user = 'transmission', password = 'transmission')
            except transmissionrpc.error.TransmissionError:
                time.sleep(60)
                count = count + 1
            else:
                break
        if count >=3:
            raise Exception("time out")

    def download_torrent(self, torrent, location):
        base_path = "/downloads/"
        abs_path = (base_path + str(location)+'/').encode('utf-8')
        if not os.path.isdir(abs_path):
            self.creat_folder(abs_path)
        #self.tc.add_torrent(torrent,download_dir=abs_path)
        transmission_add_torrent = ['/usr/bin/transmission-remote', "-n", "transmission:transmission",]
        transmission_add_torrent.append("--add")
        transmission_add_torrent.append(torrent)
        transmission_add_torrent.append("-w")
        transmission_add_torrent.append(location)
        subprocess.call(transmission_add_torrent)

    def creat_folder(self, dir):
        subprocess.call(['mkdir',dir])
        subprocess.call(['chmod', '-R', '777', dir])

    def remove_finish_torrent(self):
        import subprocess
 
        def List_Torrent():
            transmission_list = ["/usr/bin/transmission-remote -n transmission:transmission -l"]
            temp, err = subprocess.Popen(transmission_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True).communicate()
            var = []
            temp = str(temp)
            #print (temp)
            for line in temp.split('\\n'):
                print (line)
                var.append(line)
            var.pop(-1)
            var.pop(-1)
            var.pop(0)
            return var
            
        def Romove_Torrent(id):
            transmission_remove = ['/usr/bin/transmission-remote', "-n", "transmission:transmission",]
            temp = str(id)
            transmission_remove.append(temp)
            temp = '-r'
            transmission_remove.append(temp)
            subprocess.call(transmission_remove)  

        check_list =  List_Torrent()

        if not check_list:
            pass
        else:
            ID ='-t'
            for item in check_list:
                #print (temp)
                temp = item.split()
                if temp[4] == 'Done':
                    ID = ID+temp[0]+','
                else:
                    pass
            if ID != '-t':
                Romove_Torrent(ID)

    def close(self):
        self.tc = None
