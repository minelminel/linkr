from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**krwags):
    return render(request,"home.html",{})