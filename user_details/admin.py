from django.contrib import admin
from .models import Payment_Rate 
from .models import User_Payment_Details
from .models import User_Chit_Draw_Details
from .models import Monthly_Bid_Details

admin.site.register(Payment_Rate)
admin.site.register(User_Payment_Details)
admin.site.register(User_Chit_Draw_Details)
admin.site.register(Monthly_Bid_Details)




