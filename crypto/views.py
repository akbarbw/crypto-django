import requests
from django.shortcuts import render
from django.conf import settings
# Create your views here.

def index(request):
    apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    context = {'apidata': apidata}
    return render(request, 'index.html', context)