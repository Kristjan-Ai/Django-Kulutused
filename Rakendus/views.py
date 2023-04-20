from urllib.request import HTTPRedirectHandler
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(leht.html)