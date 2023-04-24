from urllib.request import HTTPRedirectHandler
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from Rakendus.models import tehing, inimene
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.template import Library

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
        if request.method=="POST":
            praegu_id = tehing.objects.get(id=request.POST.get("id"))
            andja1 = praegu_id.andja
            saaja1 = praegu_id.saaja
            kogus1 = praegu_id.kogus
            praegu_id.delete()
            a = inimene.objects.get(nimi=andja1)
            a.raha += kogus1
            a.save()
            b = inimene.objects.get(nimi=saaja1)
            b.raha -= kogus1
            b.save()
        tehingud = list(tehing.objects.all())
        inimesed = list(inimene.objects.all())
        inimesed_uus = inimesed
        for element in inimesed:
            "Siin toimub midagi kahtlast. Üks element lihtsalt kaob ära."           
            if len(tehing.objects.all().filter(andja=element.nimi))==0 and len(tehing.objects.all().filter(saaja=element.nimi))==0:
                inimesed_uus.remove(element)
        context = {
            "tehingud":tehingud,
            "inimesed":inimesed_uus,
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
        andja=request.POST.get("andja")
        saaja=request.POST.get("saaja")
        kogus=request.POST.get("kogus")
        if len(inimene.objects.all().filter(nimi=andja))==0:
            inimene(nimi=andja, raha=-int(kogus)).save()
        elif len(inimene.objects.all().filter(nimi=andja))>0:
            juurdepääs = inimene.objects.get(nimi=andja)
            juurdepääs.raha-=int(kogus)
            juurdepääs.save()            
        if len(inimene.objects.all().filter(nimi=saaja))==0:
            inimene(nimi=saaja, raha=kogus).save()
        elif len(inimene.objects.all().filter(nimi=saaja))>0:
            juurdepääs = inimene.objects.get(nimi=saaja)
            juurdepääs.raha+=int(kogus)
            juurdepääs.save()
        uus_tehing = tehing(andja=andja, saaja=saaja, kogus=kogus)
        uus_tehing.save()                       
        return render(request, "Rakendus/index.html", {"sonum":"Tehing salvestati edukalt!"})
    else:
        return HttpResponseRedirect(reverse("login_form"))
