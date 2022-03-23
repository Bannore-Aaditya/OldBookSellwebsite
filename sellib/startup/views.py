from contextvars import Context
import email
from email import message
from logging.config import valid_ident
from multiprocessing import context
from os import name
from pickle import FALSE
from tabnanny import check
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .forms import PostForm
from .models import Books,customer

checks =False ;
# Create your views here.
def home(request):
    
    # price_lh = request.GET.get('q','price_lh');
    # price_hl = request.GET.get('q','price_hl');
    # date_ld = request.GET.get('q','date_ld');
    # date_od = request.GET.get('q','date_od');      
    # if price_lh:
    #     bookd = Books.objects.filter(soldb=False).order_by('exptp')
    
    # elif price_hl:
    #     bookd = Books.objects.filter(soldb=False).order_by('-exptp')
    
    # elif date_ld:
    #     bookd = Books.objects.filter(soldb=False).order_by('-doi')    
    
    # elif date_od:
    #     bookd = Books.objects.filter(soldb=False).order_by('doi')
    
    # else: 
        
    bookd = Books.objects.filter(soldb=False)
    
    return render(request,'home.html',{'books' : bookd});

def price_lh(request):
    bookd = Books.objects.filter(soldb=False).order_by('exptp')
    return render(request,'home.html',{'books' : bookd});

def price_hl(request):
    bookd = Books.objects.filter(soldb=False).order_by('-exptp')
    return render(request,'home.html',{'books' : bookd});

def date_ld(request):
    bookd = Books.objects.filter(soldb=False).order_by('-doi')    
    return render(request,'home.html',{'books' : bookd});

def date_od(request):
    bookd = Books.objects.filter(soldb=False).order_by('doi')    
    return render(request,'home.html',{'books' : bookd});

def contactus(request):
    return render(request,'contactus.html');
    
def aboutus(request):
    return render(request,'aboutus.html');

def followus(request):
    return render(request,'followus.html');
    




def instruction(request):
    return render(request,'instruction.html');

def register(request):
    return render(request,'register.html');

def confreg(request):
    
    if request.method == "POST" :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        phno = request.POST['phno']
        col = request.POST['col']
        
        if password1 == password2:
            if customer.objects.filter(email=email).exists():
                messages.info(request,'Emailid taken')
                return render(request,'register.html');
            else:
                cust = customer(first_name=first_name,last_name=last_name,city=city,password1=password1,password2=password2,email=email,phno=phno,col=col)
                cust.save()
                return render(request,'confreg.html');
        else:
            messages.info(request,"password not matching ")
            return render(request,'register.html');

def loginin(request):
    if request.method=='POST' :
        email = request.POST['email']
        password = request.POST['password']
        if customer.objects.filter(email=email,password1=password).exists():
            obj = customer.objects.get(email = email)
            global val 
            def val():
                return obj.id 
            return render(request,'sell.html');
                
    else:
        return render(request,'loginin.html');

def confsell(request):
     
    if request.method == "POST" :
        bname = request.POST['bname']
        author = request.POST['author']
        resalen = request.POST['resalen']
        yearofb = request.POST['yearofb']
        cond = request.POST['cond']
        exptp = request.POST['exptp']
        
        
        imp = val()
        obj = customer.objects.get(id = imp)
        
        
    book = Books(bname=bname,author=author,resalen=resalen,yearofb=yearofb,cond=cond,exptp=exptp,phnob=obj.phno,colb=obj.col,cityb=obj.city)
    book.save()
    
    return render(request,'confsell.html');    
    
def myprofile(request):
    return render(request,'myprofile.html');

def logout(request):
    check = False
    return render(request,'home.html');

    
    