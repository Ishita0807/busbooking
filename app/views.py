from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app.models import bus
from django.http import HttpResponse
from django.contrib import messages
import json
def view(request):
    print(request.session.get('current_user'))
    return render(request,'index.html')

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            user_data= "{'username':'"+user.username+"','email':'"+user.email+"'}"
            request.session['current_user']=json.dumps(user_data)
            return redirect('/')#NOT DEFINED PATH
        else:
            messages.add_message(request,messages.ERROR,"Invalid Credentials")
            return redirect('../signin/')
    return render(request,'signin.html')

def signup(request):
    
    return render(request,'signup.html')

#render signup 
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('../signin/')
    return redirect(request,'signup.html')

def product(request,id):
    bus1=bus.objects.get(id=id)
    return render(request,'tickets.html',{'bus':bus1})#UNDEFINED TICKETS.HTML

def busdets(request):
    if request.method=="POST":
        username=request.POST['username']
        bus_number=request.POST['bus_number']
        start=request.POST['start']
        end=request.POST['end']
        date=request.POST['date']
        bus1=bus(user=request.user,username=username,bus_number=bus_number,start=start,end=end,date=date)
        bus1.save()
        return redirect('store')#UNDEFINED PATH store
    return render(request,'busdets.html')

def logout(request):
    request.session.clear()
    return redirect('../signin/')#UNDEFINED PATH signin