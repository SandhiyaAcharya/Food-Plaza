from django.db import models

# Create your models here.
class Food(models.Model):
    foodId=models.AutoField(primary_key=True)
    foodName= models.CharField(max_length=30)
    foodCat=models.CharField(max_length=50)
    foodType=models.CharField(max_length=15,default="Indian")
    foodPrice=models.FloatField(max_length=15)
    foodQuantity=models.IntegerField(default=0)
    foodImage=models.ImageField(upload_to="media",default="")

    class Meta:
        db_table="Food"

class Customer(models.Model):
    customerId=models.AutoField(primary_key=True)
    customerName= models.CharField(max_length=30)
    customerEmail= models.CharField(max_length=30)
    customerPassword= models.CharField(max_length=30)
    customerContact= models.CharField(max_length=30)
    customerAddress= models.CharField(max_length=50)

    class Meta:
        db_table="Customer"

class Admin(models.Model):
    adminName=models.CharField(primary_key=True,max_length=10)
    adminPass=models.CharField(max_length=10)

    class Meta:
        db_table="Admin"

class cart(models.Model):
    cartId=models.AutoField(primary_key=True)
    custEmail=models.CharField(max_length=30)
    fid=models.IntegerField()
    foodQty=models.IntegerField(default=1)
    total=models.IntegerField(default=0, null= True)

    class Meta:
        db_table="cart"

class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    custemail = models.CharField(max_length=30)
    totalbill = models.IntegerField()
    date = models.CharField(max_length=30)
    class Meta:
        db_table = "Orders"

class orderSummary(models.Model):
    foodId=models.IntegerField()
    ordId=models.IntegerField()
    foodQuant=models.IntegerField()
    price=models.FloatField()

    class Meta:
        db_table="orderSummary"