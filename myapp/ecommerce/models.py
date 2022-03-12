from django.db import models

# Create your models here.

class Category(models.Model) :
    name=models.CharField(max_length=200)
    prioty=models.IntegerField(default=0)
    status=models.IntegerField(default=0)
class Product(models.Model):
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    price=models.DecimalField( max_digits=5, decimal_places=2,default=0.0)
    sale_price=models.DecimalField( max_digits=5, decimal_places=2,default=0.0)
    description=models.TextField()
    image_list=models.TextField()
    status=models.IntegerField(default=0)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class Account(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    status=models.DecimalField(max_digits=5, decimal_places=2,default=0)

class Blog(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    sumary = models.CharField(max_length=200)
    description = models.TextField()
    status=models.DecimalField(max_digits=5, decimal_places=2,default=0)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

class Order(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    note=models.TextField()
    status=models.DecimalField(max_digits=5, decimal_places=2,default=0)
    account_id=models.ForeignKey(Account,on_delete=models.CASCADE)


class Order_Detail(models.Model):
    quantity=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=15,decimal_places=2,default=0)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
