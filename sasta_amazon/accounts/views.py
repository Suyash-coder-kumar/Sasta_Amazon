from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,form.errors)

    else:
        form=AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})


def user_register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            return redirect('login')
        else:
            messages.error(request,form.errors)

    else:
        form=UserCreationForm()

    return render(request,'register.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')
