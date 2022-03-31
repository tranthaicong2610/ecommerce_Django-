from django.urls import  path
from . import views

app_name="ecommerce"
urlpatterns=[
    path('',views.index,name="index"),
    path('login/', views.loginUser.as_view(), name='login'),
    path('register/', views.register.as_view(), name="register"),
    path('details/<int:productid>', views.details, name='details'),
    path('contact/',views.contact,name='contact'),

]