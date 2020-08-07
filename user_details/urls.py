from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('payment_rates', views.payment_rates, name='payment_rates'),
    path('user_payments', views.user_payments, name ='user_payments'),
    path('user_chit_draw_details', views.user_chit_draw_details, name='user_chit_draw_details'),
    path('monthly_bid_details', views.monthly_bid_details, name='monthly_bid_details'),
    ]
