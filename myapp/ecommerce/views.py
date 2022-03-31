from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category
from .forms import registerForm
from .forms import  loginForm
from django.contrib.auth import authenticate,login
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.
class register(View):
    def get(self,request):
        rF = registerForm
        return render(request, 'register.html', {'rF': rF})
    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('/login/')
class loginUser(View):
    def get(self,request):
        lF=loginForm
        context={'lF':lF}
        return render(request,'login.html',context)
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user=authenticate(request,username=username,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('login fail')

def index(request):
    list_pro=Product.objects.filter(status=1)[:3]
    list_pro1=Product.objects.filter(status=0)[:3]
    list_pro2=Product.objects.filter(status=2)[:3]
    list_pro3=Product.objects.filter(status=3)[:3]
    context={'products1':list_pro,'products2':list_pro1,'products3':list_pro2,'products4':list_pro3}
    return render(request,'shop.html',context)


def details(request,productid):
    product=Product.objects.get(id=productid)
    context={'product':product}
    return render(request,'details.html',context)
def contact(request):
    return render(request,'contact.html')

