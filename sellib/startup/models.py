from distutils.command.upload import upload
import email
from multiprocessing import Condition
from pickle import TRUE
from django.db import models 
from django.db import models

# Create your models here.

class Books(models.Model):
    b_id = models.CharField(max_length=100,unique=True) 
    bname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    resalen = models.IntegerField()
    yearofb = models.IntegerField()
    cond = models.IntegerField()
    exptp = models.IntegerField()
    doi = models.DateTimeField(auto_now=True)
    phnob = models.TextField()
    colb = models.CharField(max_length=25)
    cityb = models.CharField(max_length=25)
    soldb = models.BooleanField(default=False) 
    
class customer(models.Model):
    c_id = models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    password1 = models.TextField(default="A1!b")
    password2 = models.TextField(default="A1!b")
    phno = models.PositiveBigIntegerField()
    col = models.TextField()
    city = models.TextField()

    