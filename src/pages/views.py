from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**krwags):
    return render(request, "home.html", {})

def about_view(request,*args,**krwags):
    my_context = {
        "my_text": "this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 456, 789]
    }
    return render(request, "about.html", my_context)

def contact_view(request,*args,**krwags):
    return render(request, "contact.html", {})