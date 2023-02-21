from django.shortcuts import render
from .models import *
# Create your views here.
import datetime
def home (request ):
    dates = [str(datetime.date.today() + datetime.timedelta(i)) for i in range(5)]
    print(dates)
    return render(request,"home.html",{"dates":dates})

def rutesView (request ,date):
    rutesList= rutes.objects.filter(bus_date=date)
    return render(request,"rutes.html",{'date':date,"rutes":rutesList})
def weather(request ,rute):
    
    return render(request,"weather.html",{})