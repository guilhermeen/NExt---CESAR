from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_home, name='redirect_home'),
    path('home/', views.home, name='home'),
    path('latenciaCliente/', views.latenciaCliente, name='latenciaCliente'), 
    path('returnLatenciaCliente', views.returnLatenciaCliente, name='returnLatenciaCliente'),
    path('falhas/', views.falhas, name='falhas'),
    path('returnFalhas/', views.returnFalhas, name='returnFalhas'),
    path('ataques/', views.ataques, name='ataques'),
    path('returnAtaques/', views.returnAtaques, name='returnAtaques'),
    path('latenciaAPI/', views.latenciaAPI, name='latenciaAPI'), 
    path('returnLatenciaAPI', views.returnLatenciaAPI, name='returnLatenciaAPI'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('returnUsuarios/', views.returnUsuarios, name='returnUsuarios'),
    path('novosUsuarios/', views.novosUsuarios, name='novosUsuarios'),
    path('returnNovosUsuarios', views.returnNovosUsuarios, name='returnNovosUsuarios'),
    path('acessos/', views.acessos, name='acessos'), 
    path('returnAcessos/', views.returnAcessos, name='returnAcessos'),
    path('vendas/', views.vendas, name='vendas'),
    path('returnVendas/', views.returnVendas, name='returnVendas'),
]