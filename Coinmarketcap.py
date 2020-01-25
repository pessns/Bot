from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


def get_btc():

    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '1',
        'convert': 'USD,BTC'
      }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'personal_info',  # enter API KEY HERE
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        name = data['data'][0]['name']
        price = data['data'][0]['quote']['USD']['price']
        change = data['data'][0]['quote']['USD']['percent_change_24h']
        return name, price, change
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)



def get_eth():

    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '2',
        'limit': '1',
        'convert': 'USD,ETH'
      }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '7149e60a-23d6-4108-8628-13ff9bb1718c',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        name = data['data'][0]['name']
        price = data['data'][0]['quote']['USD']['price']
        change = data['data'][0]['quote']['USD']['percent_change_24h']
        return name, price, change
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def eth(bot, update):
    info_e = get_eth()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=info_e)


def btc(bot, update):
    info_b = get_btc()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=info_b)


def main():
    updater = Updater('Sorry, this info is personal')  # Enter key for your bot
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('btc', btc))
    dp.add_handler(CommandHandler('eth', eth))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()

input('Press enter to exit')