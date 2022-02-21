from django.shortcuts import render, HttpResponse
import requests
import json
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def wrapper(request, url):
    coin_exchange = json.loads(requests.get(url).text)
    coin_name = list(coin_exchange.keys())[0]
    coin_price = float(coin_exchange[coin_name]["usd"])
    data = {"name": coin_name, "price": coin_price}
    return render(request, 'cryptoapp/cur.html', context=data)


def home(request):
    return render(request, 'cryptoapp/home.html')


def bitcoin(request):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    return wrapper(request, url)


def ethereum(request):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    return wrapper(request, url)


def tether(request):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd"
    return wrapper(request, url)
