from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpages(request):
     LWO=Webpage.objects.all()
     d={'LWO':LWO}
     return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)