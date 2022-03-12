from django.contrib import admin
from .models import Category,Product,Order,Order_Detail,Blog,Account
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Detail)
admin.site.register(Blog)
admin.site.register(Account)
