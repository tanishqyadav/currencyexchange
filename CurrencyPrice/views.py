from django.shortcuts import render
from urllib import response
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from bs4 import BeautifulSoup
import lxml
import re

@api_view(['GET'])
def Currency_scrap(request):
    currency_url = 'https://www.x-rates.com/table/?from=INR&amount=1'
    source44 = requests.get(currency_url)
    soup44 = BeautifulSoup(source44.text, 'lxml')
    # it44 = soup44.getText()
    data = []
    table = soup44.find('table', {'class': 'tablesorter ratesTable'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    d = {}
    for i in range(len(data)):
        d.update({data[i][0]: data[i][1]})


    while(True):
        return JsonResponse(d ,safe=False)
        
        
        

        
