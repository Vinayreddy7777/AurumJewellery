"""
URL configuration for Aurum_Jewellery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#created apps
from Aurum_Jewelleryapp import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #main
    path('',main_views.main_home, name='main_home'),
    path('main-about',main_views.main_about, name='main_about'),
    path('main-jewellery',main_views.main_jewellery, name='main_jewellery'),
    path('main-admin',main_views.main_admin, name='main_admin'),
    path('main-serviceproviders',main_views.main_sp, name='main_sp'),
    path('main-user',main_views.main_user, name='main_user'),
    path('main-forgotpassword',main_views.main_fp, name='main_fp'),
    path('main-otp',main_views.main_otp, name='main_otp'),
    path('main-resetpassword',main_views.main_resetpassword, name='main_resetpassword'),
    path('main-register',main_views.main_register, name='main_register'),    
    path('main-contact',main_views.main_contact, name='main_contact'),    
    path('main-chatbot',main_views.main_chatbot, name='main_chatbot'),
    
    #user
    path('user-home',main_views.user_home, name='user_home'),
]
