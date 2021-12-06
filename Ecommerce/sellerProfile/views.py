from django.shortcuts import render , redirect
from django.http import HttpResponse
from home.models import Product,Order
# Create your views here.

def sellerProfile (request):
    return render(request,"sellerprofile/sellerprofile.html")


def addNewProduct (request):

    name=request.POST["name"]
    price=request.POST["price"]

    category=request.POST["category"]
    description=request.POST["description"]
    image=request.FILES["image"]
    seller = request.user
    newproduct = Product(name=name,description=description,price=price,image=image, category= category,seller=seller)
    newproduct.save()
    

    return redirect("/sellerprofile")


def buyproduct(request):
    customer=request.user
    order, created=Order.objects.get_or_create(customer=customer,complete=False)
    items=order.orderitem_set.all()
    for item in items:
        print(item.product.price)

def addcredits (request):
    
    
    credits=request.POST["credits"]
    request.user.user.credits += credits

    
    

    return redirect("/sellerprofile")
