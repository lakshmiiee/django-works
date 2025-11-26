"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from project1 import views

urlpatterns = [
    path("",views.greeting),
    path("aboutus", views.aboutus),
    path("gallery", views.gallery),
    path("contact",views.contact),
    path("employee",views.employee),
    path('students',views.students),
    path('form',views.form),
    path('formdata',views.form),
    path('formpost',views.formpost),
    path('formdatapost',views.formpost),
    path('login',views.login),
    path('registration',views.reg),
    path('modelform',views.modelform),
    path('modelpostform',views.modelform),
    path('cust',views.cust),
    path('custfiltered',views.custfiltered),

]
