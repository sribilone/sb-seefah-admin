from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class Topic(models.Model):
#     name = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name


# class Room(models.Model):
#     host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) #1 topic has 1 room
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     # participants = 
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-updated', '-created']
    
#     def __str__(self):
#         return self.name
    
    
# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.body[0:50]

# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)

#     avatar = models.ImageField(null=True, default="avatar.svg")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class server_conf(models.Model):
    name = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    port = models.CharField(max_length=4)
    database_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class dim_sale_ordertransaction(models.Model):
    transcomp_id = models.IntegerField()
    shop_id = models.IntegerField()
    opentime = models.TimeField()
    paidtime = models.TimeField()
    salemode = models.PositiveSmallIntegerField()
    nocustomer = models.PositiveSmallIntegerField()
    table_id = models.IntegerField()
    totalretailprice = models.FloatField()
    totalretailpriceb4vat = models.FloatField()
    totalretailpricevat = models.FloatField()
    discountprice = models.FloatField()
    discountb4vat = models.FloatField()
    totalamout = models.FloatField()
    shopname = models.CharField(max_length=200)
    membercode = models.CharField(max_length=200)
    posshop_id = models.IntegerField()
    product_id = models.IntegerField() 
    product_id = models.IntegerField()
    calender_id = models.IntegerField() 
    

    