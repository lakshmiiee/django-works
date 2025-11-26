from django.urls import path
from .import views

urlpatterns = [
    path('studhome',views.studhome,name='studhome'),
    path('list', views.studentslist, name='studentslist'),
    path('form', views.studentsform, name='studentsform'),
]
