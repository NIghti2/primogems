import requests
from bs4 import BeautifulSoup

import lxml
from time import sleep
import telebot

url = 'https://landofgames.ru/articles/guides/9832-promokody-dlya-genshin-impact-kamni-istoka-ochki-priklyucheniy-i-mora.html'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
           'Accept':'image / webp, image / apng, image / svg + xml, image / *, * / *;q = 0.8'}

def parser1(url='https://landofgames.ru/articles/guides/9832-promokody-dlya-genshin-impact-kamni-istoka-ochki-priklyucheniy-i-mora.html'):
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    a = soup.find_all('div', class_="text ru p-l")
    for i in a:
        g = i.find('ul').text
        return g
lst = []
def cheacker(lst=lst):
    if parser1() in lst:

        return False

    else:
        lst.append(parser1())

        return True


# Инициализация телеграм бота
bot = telebot.TeleBot('5175620501:AAHK5743qMFEaWBYXDbp4VH3rsgytYofXrk')

@bot.message_handler()
def main(message):
    while True:
        if cheacker():
            bot.send_message(message.chat.id, f'{parser1()}')
        else:
            sleep(3600)
bot.polling(none_stop=True)
