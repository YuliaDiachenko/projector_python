import requests
import random
import json
import Tokens
import telebot

def giphy(message) -> str:

    Url = "http://api.giphy.com/v1/gifs/search?"
    API_KEY = Tokens.API_KEY_GIPHY
    query = "&q=" + message.text
    offset = f"&offset={random.randint(0, 1500)}"
    url_request = Url + API_KEY + query + offset

    try:
        response = requests.get(url_request)
        t=response.text
        data = json.loads(t)
        url_giphy_result = data["data"][0]["url"]
        return url_giphy_result
    except Exception:
        return ("It can not be a search world. Enter something else.")



bot = telebot.TeleBot(Tokens.token_telegram)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Enter a search word: ")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, giphy(message))

bot.infinity_polling()
