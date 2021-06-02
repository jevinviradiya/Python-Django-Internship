from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name="home"),
    path('about',views.aboutpageview,name="about"),
    path('contact',views.contactpageview,name="contact"),
]