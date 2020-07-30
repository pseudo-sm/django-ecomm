from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Product,Customer,Cart
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

def products(request):
    products = Product.objects.all()
    return render(request,"products.html",{"products":products})

def login(request):
    return render(request,"login.html")

def login_action(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    customer = Customer.objects.filter(username=username,password=password)
    if len(customer) > 0:
        customer=customer[0]
        request.session["active-user"] = customer.id
        return HttpResponse('Welcome user :) '+customer.first_name)
    else:
        return HttpResponse("User not found")

def add_cart(request):
    customer_id = request.session["active-user"]
    product_id = request.GET.get("product")
    quantity = request.GET.get("count")
    customer = Customer.objects.get(id=customer_id)
    product = Product.objects.get(id=product_id)
    new_cart_item = Cart(customer=customer,product=product,quantity=quantity)
    new_cart_item.save()
    # The below line does the same as the above two combined
    # Cart.objects.create(customer=customer,product=product,quantity=quantity)
    return JsonResponse(True,safe=False)
