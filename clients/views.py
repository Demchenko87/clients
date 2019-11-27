from django.shortcuts import render
from django.http import HttpResponse

def  clients_list(request):
    return HttpResponse("<h1>TEST1</h2>")