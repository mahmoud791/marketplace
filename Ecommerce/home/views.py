from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse, response
import json

from home.serializer import *
from .models import *
from authentication.models import user
from rest_framework.response import Response
from rest_framework.decorators import api_view


items = Product.objects.all()

def homePage(request):
    context = {
        "items":items
    }

    return render(request,'home/homePage.html',context)


def user_profile(request):
    seller_products = Product.objects.filter(seller=request.user)
    credits = request.user.user.credits
    context = {
        'items' : seller_products,
        'credits':credits
    }
    return render(request, 'profile/profile.html', context)

def category(request,category):
    items = {}
    if category =='clothes':
        items = Product.objects.filter(category='clothes')
    elif category=='shoes':
        items = Product.objects.filter(category='shoes')
    elif category=='watches':
        items = Product.objects.filter(category='watches')
    elif category=='laptops':
        items = Product.objects.filter(category='laptops')
    elif category=='mobile_phones':
        items = Product.objects.filter(category='mobile phones')
    elif category=='headphones&headsets':
        items = Product.objects.filter(category='headphones/headsets')
    elif category=='perfumes&deodrants':
        items = Product.objects.filter(category='perfumes/deodrants')
    elif category=='accessories':
        items = Product.objects.filter(category='accessories')
    elif category=='kid_toys':
        items = Product.objects.filter(category='kid toys')
    elif category == 'household':
        items = Product.objects.filter(category='HouseHold')


    context = {
        'items':items
    }
    

    return render(request,'category/category.html',context)



def cart(request):
    order=None

    if request.user.is_authenticated:
        customer=request.user
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
    
    context = {'items':items,'order':order}
    return render(request, 'home/cart.html', context)

def buyproduct(request):
    customer=request.user
    order, created=Order.objects.get_or_create(customer=customer,complete=False)
    items=order.orderitem_set.all()
    totalcost = 0
    for item in items:
        totalcost = totalcost + int(item.product.price)
    
    if request.user.user.credits < totalcost:
        return redirect("/cart")
    else:
        for item in items:
            item.product.seller.user.credits = item.product.seller.user.credits + int(item.product.price)
            item.product.seller.user.save()
            item.product.seller = request.user
            item.product.save()
        
        request.user.user.credits = request.user.user.credits - totalcost
        request.user.save()




        
    return redirect("/profile")


def checkout(request):
    order=None
    if request.user.is_authenticated:
        customer=request.user
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
    
    context = {'items':items,'order':order}
    return render(request, 'home/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('Action: ',action)
    print('productId: ',productId)

    customer= request.user
    product=Product.objects.get(id=productId)
    order, created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem ,created=OrderItem.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)


def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug)
    context = {
        'product': product
    }
    

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', slug=slug)

    return render(request,'home/product_detail.html',context)
def addNewProduct (request):

    name=request.POST["name"]
    price=request.POST["price"]

    category=request.POST["category"]
    description=request.POST["description"]
    image=request.FILES["image"]
    seller = request.user
    newproduct = Product(name=name,description=description,price=price,image=image, category= category,seller=seller)
    newproduct.save()
    
    

    return redirect("/profile")


def addcredits (request):
        
    
    credits=request.POST["credits"]
    
    request.user.user.credits = request.user.user.credits + int(credits)
    
    request.user.save()

    
    

    return redirect("/profile")


def search(request):
    q = request.GET.get('q')
    products = Product.objects.filter(name__icontains=q)
    context = {'query' : q, 'products' : products}
    tempelate = 'home/search.html'
    return render(request,tempelate,context)

@api_view()
def product_list(request):
    products=Product.objects.all()
    serializer = [productserializer(products, many = True).data , product2serializer(products, many = True).data]
    return Response(serializer)