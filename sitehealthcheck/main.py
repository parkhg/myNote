# coding=utf-8
"""
idleCat : HomePage Information Monitering Daemon.
Writer  : parkhg@gmail.com

pip install python-telegram-bot --upgrade

"""

import time
import datetime
import logging

import os
import signal
import argparse

import http.client
import json
import urllib.request
import telegram

class WatchCat:
    def __init__(self, log_file=None):
        sFormat = '%(asctime)-15s %(levelname)4s [%(funcName)s] %(message)s'
        logging.basicConfig(level=logging.INFO, format=sFormat)

        self.logger = logging.getLogger("idleCat")
        self.log_file = log_file

        if log_file:
            self.log_handler = logging.FileHandler(self.log_file)
            self.logger.addHandler(self.log_handler)

        self.__stop = False

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

    def main(self):
        isDown = False
        self.botsendmessage("=^.^=, Start idleCat...")
        self.logger.info("Start idleCat, PID {0}".format(os.getpid()))

        status = self.sitehealthcheck("www.wu.ac.kr")
        if status == 'on':
            self.botsendmessage("=^.^=, I'm Ok. play with me.")

        msg = self.applydata()
        self.botsendmessage(msg)

        while not self.__stop:
            now = datetime.datetime.now() + datetime.timedelta(hours=9)   # Google서버 USA time.
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
            nowHH = now.strftime('%H')
            nowMM = now.strftime('%M')
            # print(nowTime)        # 12:11

            # msg = self.applydata()
            # self.botsendmessage(msg)

            status = self.sitehealthcheck("www.wu.ac.kr")
            self.logger.info('Homepage Health Check : ' + status)

            if status == 'on':
                 # System 복구
                if isDown == True:
                    self.botsendmessage("=^.^=, I got up. play with me.")
                    isDown = False
            else:
                # Msg를 한번만 발송
                if isDown == False:
                    self.botsendmessage('Oops!\nHomepage Down, \nHurry Up!!!\n' + nowDatetime)
                    isDown = True

            # Demon 실행 중...
            if nowHH in ('08','20') and nowMM in ('00','01','02','03','04'):
                self.botsendmessage('ㄴ(=^.^=)ㄱ')

            # 원서접수 현황
            if nowHH in ('08','12','19','20') and nowMM in ('00','01','02','03','04'):
                msg = '[수시1차 원서접수]\n' + self.applydata() + '\n' + nowDatetime
                self.botsendmessage(msg)

            time.sleep(300)

    def stop(self, signum, frame):
        self.__stop = True
        self.logger.info("Receive Signal {0}".format(signum))
        self.logger.info("Stop idleCat")

    def sitehealthcheck(self, url):
        try:
            conn = http.client.HTTPConnection(url)
            conn.request("HEAD", "/")
            r1 = conn.getresponse()
            self.logger.info('Site Health Status : ' + r1.reason)
            if getattr(r1,'status') == 200:
                conn.close()
                return 'on'

        except http.client.HTTPException:
            self.logger.info('http Error : ' + http.client.HTTPException)
            conn.close()
            return 'off'

        except:
            self.logger.info('Bad URL : ' + url)
            return 'off'

    def applydata(self):
        url = "https://odin.wu.ac.kr:8443/_odin/web/applydata.jsp"

        req = urllib.request.Request(url, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(req)
        jsonString = response.read().decode('euc-kr')   # decode: 바이트를 문자열로 변환
        # print(jsonString)
        mydata = json.loads(jsonString)

        msg = ''
        num = len(list(mydata))
        for i in range(0,num):
            mylist = mydata[i]
            msg += "{0:<10}".format(mylist['name']) + ' : ' +  mylist['cnt'] + '\n'

        print(msg)
        return msg

    def botsendmessage(self, msg):
        # boricat
        mytoken = '669073981:AAHI2uug1CqRabD1V30pn8bkfHuDNCDDJD0'
        bot = telegram.Bot(token = mytoken)
        bot.sendMessage(chat_id = "@boricat", text=msg)

        # idleCat
        # mytoken = '643231881:AAGtXcshvygRb1dGcN9fglbkMSCpnPV7Goo'
        # bot = telegram.Bot(token = mytoken)
        # bot.sendMessage(chat_id = "@idle_cat", text=msg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", help="log filename", default=None)
    args = parser.parse_args()

    idleCat = WatchCat()
    idleCat.main()
