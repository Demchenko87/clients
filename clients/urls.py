from django.urls import path
from .views import *

urlpatterns = [
    path('', clients_list)
]