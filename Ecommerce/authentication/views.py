from django.shortcuts import render , redirect
from django.http import HttpResponse
from authentication.models import user
from django.contrib.auth import authenticate, login, logout

from home import serializer
from .forms import NewUser
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication.serializer import *
from django.contrib.auth.models import User



def login_page (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    context = {}        
    return render(request,'login/login.html' ,context)

def log_out(request):
    logout(request)
    return redirect('home')

def register (request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # u_profile = profile.objects.create(user=user)
            # u_profile.is_seller = request.POST.get('is_seller')
            # u_profile.save()
            messages.success(request, f'{user} has been successfully created.')
            return redirect('login')
    context = {'form' : form}
    return render(request,'register/register.html',context)

def test_user_creation (request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user.capitalize()} has been successfully created.')
    context = {'form' : form }
    return render(request,'testing/createuser.html',context)


@api_view()
def User_list(request):
    users=request.user
    serializer1 = Userserializer(users)
    serializer2 = userserializer(users)
    serializer = [serializer1.data , serializer2.data]
    return  Response(serializer)

