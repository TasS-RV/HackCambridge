from .scripts.scrapy.crawl_script import crawl_query

# Create your views here. Function taking request, and returns and output - 'action', called 'view' in django
#Normally 'template' what a user sees in django
from django.shortcuts import render
from django.http import HttpResponse

import logging

logger = logging.getLogger()

def say_hello(request):
    x = 1
    y = 2

#    return HttpResponse("Hello User")
    return render(request, 'greeting.html', {'name': 'Tas'})
#Renders based on html from the template

#Get rid of this to make it work - might need the functions within a class...
def company_input(request):
    key = 'company_query'
    if key in request.POST:
        logger.info('POST request received.')
        crawl_query(request.POST[key], "environmental")
    return render(request, 'index.html')

