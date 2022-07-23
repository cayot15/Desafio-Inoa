from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # path da pagina principal
    path('home/add/', views.home_add, name='home_add'),  # path que adiciona
    path('home/delete/<int:stock_pk>', views.home_delete, name='home_delete'),  # path que deleta
    path('home/edit/<int:stock_pk>', views.home_edit, name='home_edit')  # path que edita

]
