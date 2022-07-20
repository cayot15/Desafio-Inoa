from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/add/', views.home_add, name='home_add'),
    path('home/delete/<int:stock_pk>', views.home_delete, name='home_delete'),
    path('email/', views.envia_email, name='envia_email')

]
