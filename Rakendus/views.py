from urllib.request import HTTPRedirectHandler
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from Rakendus.models import tehing
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def login_(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Rakendus/login.html", {"sonum":"Vale parool või kasutajanimi!"})
        
def login_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Rakendus/login.html")
    
def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_form"))
    
def index(request):
    if request.user.is_authenticated:
        return render(request, "Rakendus/index.html")
    else:
        return HttpResponseRedirect(reverse("login_form"))
    
def praegu(request):
    if request.user.is_authenticated:
        tehingud = list(tehing.objects.all())
        if request.method=="POST":
            tehing.objects.get(id=request.POST.get("id")).delete()
        context = {
            "tehingud":tehingud,
        }                      
        return render(request, "Rakendus/praegu.html", context)
    else:
        return HttpResponseRedirect(reverse("login_form"))
    
def sisestus(request):
    if request.user.is_authenticated:
        return render(request, "Rakendus/sisestus.html")
    else:
        return HttpResponseRedirect(reverse("login_form"))

def tegele(request):
    if request.user.is_authenticated:
        uus_tehing = tehing(andja=request.POST.get("andja"), saaja=request.POST.get("saaja"), kogus=request.POST.get("kogus"))
        uus_tehing.save()
        return render(request, "Rakendus/index.html", {"sonum":"Tehing salvestati edukalt!"})
    else:
        return HttpResponseRedirect(reverse("login_form"))
