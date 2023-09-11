from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        userName=request.POST['userName']
        fName=request.POST['FName']
        LName=request.POST['LName']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        if User.objects.filter(username=userName):
            messages.error(request,"Username already exists \n ! Please try some other username.")
            return redirect('home')


        if len(userName)>10:
            messages.error(request,"username must be under 10 characters")            

        if pass1 !=pass2:
            messages.error(request,"Passwords did't match")            
        myuser=User.objects.create_user(userName,pass1,pass2)

        myuser.first_name=fName
        myuser.last_name=LName

        myuser.save()
        
        messages.success(request,"Your Account has been created Succussfully .")

        return redirect('signin')
    return render(request,"signup.html")    

def signin(request):
    if request.method=="POST":
        username=request.POST['userName']
        pass1=request.POST['pass1']
        
        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fName=user.first_name
            return render(request,"index.html",{'fName':fName})

        else:
            messages.error(request,"Bad Credentials !!")            
            return render(request,"next.html")
    return render(request,"signin.html")    

def signout(request):
    logout(request)
    messages.success(request,"Logout Successfully !!!")
    return redirect('home')
              