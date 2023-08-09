import requests
import random
import json

Url = "http://api.giphy.com/v1/gifs/search?"

API_KEY = "api_key=Hoj7s0jtY0mJfU8EOABcvQkWCZe1WELT"
query = "&q=" + input("Enter a search word: ")
offset = f"&offset={random.randint(0, 1500)}"

url_request = Url + API_KEY + query + offset
try:
    response = requests.get(url_request)
    t=response.text
    data = json.loads(t)
    url_giphy_result = data["data"][0]["url"]
    print(url_giphy_result)
except Exception:
    print("It can not be a search world. Enter something else.")

"""
Done! Congratulations on your new bot. You will find it at t.me/giphy1_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5645594223:AAEzCd_FHPmSS5ARZFmW14jJ6K3emqCA7i4
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
"""
