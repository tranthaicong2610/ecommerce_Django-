from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category

# Create your views here.
def index(request):
    list_pro=Product.objects.filter(status=1)[:3]
    list_pro1=Product.objects.filter(status=0)[:3]
    list_pro2=Product.objects.filter(status=2)[:3]
    list_pro3=Product.objects.filter(status=3)[:3]
    context={'products1':list_pro,'products2':list_pro1,'products3':list_pro2,'products4':list_pro3}
    return render(request,'shop.html',context)
def login(request):
    return render(request,'login.html');