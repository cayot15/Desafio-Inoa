from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/add/', views.home_add, name='home_add'),
    path('Stocks/', views.Stocks, name='Stocks'),
    path('Closeprice/', views.Closeprice, name='Closeprice')

]
