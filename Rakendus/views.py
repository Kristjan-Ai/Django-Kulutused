from urllib.request import HTTPRedirectHandler
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    from os import system
    import random
    pikkus = str(random.uniform(0, 360) - 180)
    laius = str(random.uniform(0, 170) - 85)
    asukoht = "https://maps.google.com/?q="+laius+","+pikkus
    if 59.82 >= float(laius) >= 57.52 and 28.20 >= float(pikkus) >= 21.76:
        asukoht+="\nEESTI!!!"
#        print(asukoht)
#        input("Vajuta ENTER, et see avada!")
#        system("start "+asukoht)
#        if 59.82 >= float(laius) >= 57.52 and 28.20 >= float(pikkus) >= 21.76:
#            print("EESTI!!!")
#        system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return HttpResponse(asukoht)