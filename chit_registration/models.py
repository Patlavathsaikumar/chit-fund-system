from django.db import models

# Create your models here.
class Registration_Chit(models.Model):
    
    group_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    no_of_chits = models.IntegerField()
    mobile_number = models.BigIntegerField()
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)