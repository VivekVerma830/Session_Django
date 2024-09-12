from django.urls import path
from app .views import *

urlpatterns = [
    path('set/',set,name='set'),
    path('get/',get,name="get"),
    path('delete/', delete ,name="delete"),
    ]