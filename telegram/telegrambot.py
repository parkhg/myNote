import telegram

'''
pip install python-telegram-bot --upgrade
'''
# Bot을 위한 Token : boricat_bot
mytoken = '669073981:AAHI2uug1CqRabD1V30pn8bkfHuDNCDDJD0'

bot = telegram.Bot(token = mytoken)

updates = bot.getUpdates() # Update 내역을 받아온다.

for u in updates:
    print(u.message)

chat_id = bot.getUpdates()[-1].message.chat.id # 가장 최근 메세지의 chat id

# bot.sendMessage(chat_id = chat_id, text="I'm BoriCat.")

# Channel에 등록됨
bot.sendMessage(chat_id = "@boricat", text="I'm BoriCat. Cute Cat.")
