from django.db import models

class Payment_Rate(models.Model):
    
    month = models.IntegerField()
    total_amount = models.IntegerField()
    chit_draw_amount = models.IntegerField()
    amount_to_pay = models.IntegerField()
    commission_amount = models.IntegerField()

class User_Payment_Details(models.Model):

    username = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100) 
    May_05_2019 = models.BooleanField(default=False)
    June_05_2019 = models.BooleanField(default=False)
    July_05_2019 = models.BooleanField(default=False)
    August_05_2019 = models.BooleanField(default=False)
    September_05_2019 = models.BooleanField(default=False)
    October_05_2019 = models.BooleanField(default=False)
    November_05_2019 = models.BooleanField(default=False)
    December_05_2019 = models.BooleanField(default=False)
    January_05_2020 = models.BooleanField(default=False)
    February_05_2020 = models.BooleanField(default=False)
    March_05_2020 = models.BooleanField(default=False)
    April_05_2020 = models.BooleanField(default=False)
    May_05_2020 = models.BooleanField(default=False)
    June_05_2020 = models.BooleanField(default=False)
    July_05_2020 = models.BooleanField(default=False)
    August_05_2020 = models.BooleanField(default=False)
    September_05_2020 = models.BooleanField(default=False)
    October_05_2020 = models.BooleanField(default=False)
    November_05_2020 = models.BooleanField(default=False)
    December_05_2020 = models.BooleanField(default=False)

class User_Chit_Draw_Details(models.Model):

    username = models.CharField(max_length=100)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    month_of_bid = models.CharField(max_length=200)
    total_chit_amount_transferable =models. IntegerField()
    commission_amount = models.IntegerField()
    respective_chit_amount = models.IntegerField()
    total_received = models.IntegerField()
    customer_note = models.CharField(max_length=200)
    admin_note = models.CharField(max_length=200)

class Monthly_Bid_Details(models.Model):

    username = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    no_of_chits = models.IntegerField(default=1)
    bid_month = models.IntegerField()
    total_chit_amount = models.IntegerField()
    total_commission_amount = models.IntegerField()
    amount_to_pay = models.IntegerField()
    commission_amount = models.IntegerField()
    total_amount_to_pay = models.IntegerField()



