from django.urls import path
from . import views

urlpatterns = [
    path('teachome/', views.teachome, name='teachome'),  # THIS IS CRUCIAL
    path('list/', views.teachlist, name='teachlist'),
    path('form/', views.teachform, name='teachform'),
]

