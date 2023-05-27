from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def demo(request):
     return render(request ,"index.html")
def division(request):
     x=int(request.GET["no 1"])
     y=int(request.GET["no 2"])
     res=x/y
     return render(request,"about.html",{'result':res})