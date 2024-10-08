from django.shortcuts import render

import requests
import json


# Create your views here.

def index(request):

    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    jls_extract_var = "ip"
    res = requests.get('http://ip-api.com/json/'+ip_data[jls_extract_var])
    location_data_one = res.text
    location_data = json.loads(location_data_one)

    return render(request, 'index.html', {'data': location_data})