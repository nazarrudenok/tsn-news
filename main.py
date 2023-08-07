import telebot
import requests
from bs4 import BeautifulSoup
from time import sleep
from config import TOKEN, URL

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    cht = message.chat.id

    titles = []
    urls = []
    while True:
        r = requests.get(URL).text
        bs = BeautifulSoup(r, 'html.parser')

        news_title = bs.find_all('div', class_='c-card__body')[8].find('a').text.strip()
        news_url = bs.find_all('div', class_='c-card__body')[8].find('a')['href'].strip()

        if news_title not in titles and news_url not in urls:
            titles.append(news_title)
            urls.append(news_url)
            bot.send_message(cht, f'<b><a href="{news_url}">{news_title}</a></b>', parse_mode='HTML')
            print(titles)
        sleep(5)

bot.polling()