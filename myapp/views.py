from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
m1 = "<h1>Prueba de proyecto con DJANGO</h1>"
m2 = "<p>Fuente: https://www.youtube.com/watch?v=T1intZyhXDU&t=317s&ab_channel=Fazt</p>"
def hello(request):
    return HttpResponse(m1 + m2)