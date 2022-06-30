from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . forms import BookForm
from . models import Book


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

# create login views here

def log_in(request):
    if not request.user.is_authenticated:
        if request.method== "POST":
            us= User
            fm = AuthenticationForm(us, data=request.POST)
            if fm.is_valid():
                uemail= fm.cleaned_data['username']
                print(uemail)
                upass= fm.cleaned_data['password']
                user = authenticate(username=uemail, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/main/')
        else:
            fm=AuthenticationForm()
        return render(request, "core/login.html",{'form':fm})
    else:
        return HttpResponseRedirect('/main/')

# create main views

def main(request):
    if request.method == 'POST':
        fm=BookForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=BookForm()
    else:
        fm=BookForm()
    book= Book.objects.all()
    return render(request, 'core/main.html',{'form': fm, 'bk':book})

# create update  function

def updatebook(request,id):
    if request.method == 'POST':
        pi= Book.objects.get(pk=id)
        fm = BookForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/main/')
    else:
        pi= Book.objects.get(pk=id)
        fm = BookForm(instance=pi)
    return render(request, 'core/update.html', {'form': fm})

#delete function

def deletebook(request,id):
    if request.method == 'POST':
        delb=Book.objects.get(pk=id)
        delb.delete()
        return HttpResponseRedirect('/main/')

# create logout views here

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
