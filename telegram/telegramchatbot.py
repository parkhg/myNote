# _*_ coding : utf8 _*_

import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

mytoken = '669073981:AAHI2uug1CqRabD1V30pn8bkfHuDNCDDJD0'

print('start telegram chat bot.')

dirnow = os.path.dirname(os.path.abspath(__file__))
print('Photo Save Dir : ', dirnow)

## @brief 1. message reply function
#  @param
def get_message(bot, update):
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)

## @brief 2. help reply function
#  @param update
def help_command(bot, update):
    print('Command : ', update.message.text)
    update.message.reply_text("Why?")

## @brief 3. photo reply function
#  @param update
def get_photo(bot, update):
    print(update.message)
    filepath = os.path.join(dirnow,'from_telegram.png') # 파일 확장자 주의
    photoid = update.message.photo[-1].file_id          # photo번호가 높을수록 화질이 좋음
    photofile = bot.getFile(photoid)
    photofile.download(filepath)
    update.message.reply_text('photo saved.')


## @brief 4. file reply function
#  @param update
def get_file(bot, update):
    fileidshort = update.message.document.file_id
    fileurl = os.path.join(dirnow, update.message.document.file_name)
    bot.getFile(fileidshort).download(fileurl)
    update.message.reply_text('file saved.')


# bot의 메시지를 가져온다.
updater = Updater(mytoken)

# 1. Message Handler
# 메시지의 Filters.text에 따라 get_message가 호출된다.
message_handler = MessageHandler(Filters.text, get_message)
# handler 추가
updater.dispatcher.add_handler(message_handler)

# 2. Command 응답하기
help_handler = CommandHandler('help',help_command)
updater.dispatcher.add_handler(help_handler)

# 3. Photo 응답 및 저장하기
photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

# 4. 파일응답 및 저장하기
file_handler = MessageHandler(Filters.document, get_file)
# updater.dispatcher.add_handler(get_file)  # Error 원인 못 찾음

# polling 시간 2초, clean = true 텔레그램 서버에 저장안함
updater.start_polling(timeout=2, clean=True)
updater.idle()    # updater가 종료되지 않고 계속 실행되도록 처리함
