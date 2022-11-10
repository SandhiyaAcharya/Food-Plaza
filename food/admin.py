from django.contrib import admin
from .models import Food,Customer,Admin,cart,Orders,orderSummary

# Register your models here.
admin.site.register(Food)   
admin.site.register(Customer) 
admin.site.register(Admin)
admin.site.register(cart)
admin.site.register(Orders)
admin.site.register(orderSummary)