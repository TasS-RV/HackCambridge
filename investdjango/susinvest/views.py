
# Create your views here. Function taking request, and returns and output - 'action', called 'view' in django
#Normally 'template' what a user sees in django
from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    x = 1
    y = 2

#    return HttpResponse("Hello User")
    return render(request, 'greeting.html', {'name': 'Tas'})
#Renders based on html from the template

#Get rid of this to make it work - might need the functions within a class...
def company_input(request):
    return render(request, 'websiteentry.html')

