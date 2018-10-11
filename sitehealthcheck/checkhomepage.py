# coding=utf-8
"""
idleCat : HomePage Health Check.
Writer  : parkhg@gmail.com
"""

import logging
import http.client
import telegram

logger = logging.getLogger('idleCat')
logger.setLevel(logging.INFO)

## Check Homepage Health.
def is_on_site(url):

    try:
        conn = http.client.HTTPConnection(url)
        conn.request("HEAD", "/")
        r1 = conn.getresponse()
        logger.info('Site Health Status : ' + r1.reason)
        if getattr(r1,'status') == 200:
            conn.close()
            return 'on'

    except http.client.HTTPException:
        logger.info('http Error : ' + http.client.HTTPException)
        conn.close()
        return 'off'

    except:
        logger.info('Bad URL : ' + url)
        conn.close()
        return 'off'

def botsendmessage(msg):
    # boricat
    mytoken = '669073981:AAHI2uug1CqRabD1V30pn8bkfHuDNCDDJD0'
    bot = telegram.Bot(token = mytoken)

    bot.sendMessage(chat_id = "@boricat", text=msg)
