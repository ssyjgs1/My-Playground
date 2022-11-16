"""
import telegram as tel
import time
import datetime
import schedule
from datetime import datetime

now = datetime.now()
bot = tel.Bot(token="ㅁㅁㅁㅁㅁㅁㅁㅁ")
chat_id = ㅁㅁㅁㅁㅁㅁㅁㅁ

# 메세지 보내기
# bot.sendMessage(chat_id=chat_id, text="Test Message")

def gojen():
    bot.sendMessage(chat_id=chat_id, text="오전 출석 : https://forms.office.com/r/VACLTfSDyB")

def gogo():
    bot.sendMessage(chat_id=chat_id, text="오후 출석 : https://forms.office.com/r/5UjEDytx9S")

def owari():
    bot.sendMessage(chat_id=chat_id, text="종료 출석 : https://forms.office.com/r/988BfmDUjv")

def test():
    bot.sendMessage(chat_id=chat_id, text="테스트용입니다! https://forms.office.com/r/VACLTfSDyB")

while True:
    schedule.run_pending()
    schedule.every().day.at("08:45:00").do(gojen)
    time.sleep(59)
    
    schedule.run_pending()
    schedule.every().day.at("12:55:00").do(gogo)
    time.sleep(59)
    
    schedule.run_pending()
    schedule.every().day.at("17:51:00").do(owari)
    time.sleep(59)
"""

import telegram as tel
import time
import datetime
import schedule
from datetime import datetime

now = datetime.now()
bot = tel.Bot(token="ㅁㅁㅁㅁㅁㅁㅁㅁ")
chat_id = ㅁㅁㅁㅁㅁㅁㅁㅁㅁ

# 메세지 보내기
# bot.sendMessage(chat_id=chat_id, text="Test Message")

def gojen():
    bot.sendMessage(chat_id=chat_id, text="오전 출석 : https://forms.office.com/r/VACLTfSDyB")

def gogo():
    bot.sendMessage(chat_id=chat_id, text="오후 출석 : https://forms.office.com/r/5UjEDytx9S")

def owari():
    bot.sendMessage(chat_id=chat_id, text="종료 출석 : https://forms.office.com/r/988BfmDUjv")

def test():
    bot.sendMessage(chat_id=chat_id, text="테스트용입니다! https://forms.office.com/r/VACLTfSDyB")

while True:
    schedule.run_pending()
    schedule.every().day.at("08:45:00").do(gojen)
    time.sleep(86400)
    break

while True:
    schedule.run_pending()
    schedule.every().day.at("12:55:00").do(gogo)
    time.sleep(86400)
    break

while True:
    schedule.run_pending()
    schedule.every().day.at("17:51:00").do(owari)
    time.sleep(86400)
    break