from django.shortcuts import render
from django.http import HttpResponse
from .helpers import get_character_name, ip_info

def index(request):
    country = ip_info('country_name')
    flag = ip_info('flag')
    
    context = {
        'country': country,
        'flag': flag,
    }
    
    return render(request, 'index.html', context)