from django.shortcuts import render
from getPriceFunctions import getAnyPrice
from json import dumps
from django.http import HttpResponse

def index(request):
    price = {}
    price['price'] = getAnyPrice.getExchangePrice('coinbase')
    return HttpResponse(dumps(price))




