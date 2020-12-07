from django.contrib import admin
from django.urls import path ,include
from HOME import views

urlpatterns = [
    path('index', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('details', views.details, name='details'),
    path('order', views.order, name='order'),
    path('cart',views.cart,name='cart'),
    path('order_success',views.order_success,name='order_success'),
]