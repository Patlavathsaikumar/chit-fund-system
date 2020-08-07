from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Payment_Rate
from .models import User_Payment_Details
from .models import User_Chit_Draw_Details
from .models import Monthly_Bid_Details
import operator
from django.contrib.auth.models import User

def payment_rates(request):

    rates = Payment_Rate.objects.all()
    return render(request,"payment_rates.html", {'rates' : rates})

def user_payments(request):

    un = request.user.username
    payments = User_Payment_Details.objects.filter(username__exact=un)
    return render(request,"user_payments.html",{'payments' : payments})

def user_chit_draw_details(request):

    un = request.user.username
    if User_Chit_Draw_Details.objects.filter(username=un).exists():
        bids =  User_Chit_Draw_Details.objects.filter(username__exact=un)
        return render(request, "user_chit_draw_details.html", {'bids': bids})
    else:
        return render(request, "undrawn_chit_details.html")

def monthly_bid_details(request):

    un = request.user.username
    if Monthly_Bid_Details.objects.filter(no_of_chits__exact=1):
        amount = Monthly_Bid_Details.objects.filter(username__exact=un)
        return render(request,"monthly_bid_details_1.html",{'amount': amount})
    else:
        amount = Monthly_Bid_Details.objects.filter(username__exact=un)
        return render(request,"monthly_bid_details_2.html",{'amount': amount})