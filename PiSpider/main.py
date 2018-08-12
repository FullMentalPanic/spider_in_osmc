from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from PiSpider.transmission import *
import time
from threading import *
import RPi.GPIO as GPIO

class PiFanControl(object):
    def __init__(self):
        self.thread = Thread(target = self.run_spider_periodic, args = ())
        self.thread.daemon = True

    def start(self):
        self.thread.start()

    def run_spider_periodic(self):  #every 12 h =12*60*60 s
        while True:
            time.sleep(1*30)
            control_Fan()


    def close(self):
        self.thread.join()

    def __del__(self):
        self.thread.join()

def Shutdown(channel):
    os.system("sudo shutdown -h now")

def Check_GPU_tempture():
    get_GPU_temp = ["/opt/vc/bin/vcgencmd measure_temp"]
    temp, err = subprocess.Popen(get_GPU_temp, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True).communicate()
    temp = str(temp)
    return (float(temp[temp.index('=') + 1:temp.rindex("'")]))

def Check_CPU_tempture():
    try:
        tf = open('/sys/class/thermal/thermal_zone0/temp')
        temp =(float(tf.read())) / 1000
    except:
        temp = 0.0
    return temp

def control_Fan():
    CPU_temp = Check_CPU_tempture()
    GPU_temp = Check_GPU_tempture()

    if CPU_temp > 50.0 or GPU_temp >50.0:
        GPIO.output(26,0)
    elif CPU_temp < 45.0 and GPU_temp < 45.0:
        GPIO.output(26,1)
    else:
        pass

if __name__=="__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP) # shutdown button
    GPIO.setup(26,GPIO.OUT, initial = 1) # Fan control
    GPIO.add_event_detect(3, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

    try:
        P = PiFanControl()
        P.start()
        while True:
            remove_transmission_finish_work()
            process = CrawlerProcess(get_project_settings())
            process.crawl('dmhy_rss')
            process.start() # the script will block here until the crawling is finished
            time.sleep(12*60*60)
    except:
        P.close()
