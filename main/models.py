from django.db import models
from django import forms



# Homepage

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_worldwide = models.BooleanField(default = False)

    
    
# Services

class Solution(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length = 100)
    description = models.TextField()
    type = models.CharField(max_length = 50)


# Clients

class Client(models.Model):
    image = models.ImageField(upload_to='imags/')


# Blog

class Member(models.Model):
    image = models.ImageField(upload_to='imags/')
    name = models.CharField(max_length = 100)
    description = models.TextField()
    position = models.CharField(max_length = 50)


# Contact/Message

class Message(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField()


