#urls are views - stored at requests of user
from django.urls import path, include
from . import views  

#URL conf module - URL configuration 
urlpatterns = [
#No need to write it this way - as added on the main urls.py to redirect to thsi file    path('susinvest/greeting', views.say_hello())
path('greeting/', views.say_hello),

path('websiteentry/', views.company_input)
]
#,path('farewell/', views.farewell)


#Must remember to add a forward slash!