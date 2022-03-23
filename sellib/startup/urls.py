from django.contrib import admin
from django.urls import path
from startup import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('contactus',views.contactus,name="contactus"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('followus',views.followus,name="followus"),
    path('sell',views.loginin,name="sell"),
    path('instruction',views.instruction,name="instruction"),
    path('register',views.register,name="register"),
    path('loginin',views.loginin,name="loginin"),
    path('confsell',views.confsell,name="confsell"),
    path('confreg',views.confreg,name="confreg"),
    path('myprofile',views.myprofile,name="myprofile"),
    path('logout',views.logout,name="logout"),
    path('home/price_lh',views.price_lh,name="price_lh"),
    path('home/price_hl',views.price_hl,name="price_hl"),
    path('home/date_ld',views.date_ld,name="date_ld"),
    path('home/date_od',views.date_od,name="date_od"),
]
