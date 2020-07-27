from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

products = [
    {
        "id" : 1,
        "name" : "iPhone 6",
        "price" : "25,000",
        "image" : "iphone6.jpeg"
    },
    {
        "id" : 2,
        "name" : "iPhone 7",
        "price" : "36,000",
        "image" : "iphone7.jpeg"
    },
    {
        "id" : 3,
        "name" : "iPhone X",
        "price" : "60,000",
        "image" : "iphonex.jpg"
    }
]

def index(request):
    name = "John"
    return render(request,"index.html",{"products":products,"name":name})

