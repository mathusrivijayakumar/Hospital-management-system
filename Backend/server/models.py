from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email=models.EmailField(max_length=40)
    contact=models.BigIntegerField()
    zip=models.IntegerField()

class Doctors(models.Model):
    docid=models.AutoField(primary_key=True,unique=True)
    docname=models.CharField(max_length=40)
    specialisation=models.CharField(max_length=40)
    docemail=models.EmailField(max_length=40)
    password=models.CharField(max_length=25)
    contact=models.BigIntegerField()
    address=models.CharField(max_length=75)

class Appointments(models.Model):
    appid=models.AutoField(primary_key=True,unique=True)
    docid=models.IntegerField()
    docname=models.CharField(max_length=40)
    pid=models.IntegerField()
    pname=models.CharField(max_length=40)
    appdate=models.DateTimeField()
    desc=models.CharField(max_length=150)

class Adminlog(models.Model):
    adid=models.AutoField(primary_key=True,unique=True)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class Medrecord(models.Model):
    rid=models.AutoField(primary_key=True,unique=True)
    docid=models.IntegerField()
    docname=models.CharField(max_length=40)
    date=models.DateTimeField()
    pid=models.IntegerField()
    pname=models.CharField(max_length=40)
    age=models.IntegerField()
    bldgrp=models.CharField(max_length=5)
    desc=models.CharField(max_length=150)
    nxtapp=models.DateTimeField()
    tplan=models.CharField(max_length=200)
    

