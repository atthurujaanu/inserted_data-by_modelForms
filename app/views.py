from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse


# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic is inserted successfully')


    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WPFO=WebpageForm(request.POST)
        if WPFO.is_valid():
            WPFO.save()
            return HttpResponse('Webpage is inserted')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    AFO=AccessForm()
    d={'AFO':AFO}

    if request.method=='POST':
        ARFO=AccessForm(request.POST)
        if ARFO.is_valid():
            ARFO.save()
            return HttpResponse('access is inserted')
    return render(request,'insert_access.html',d)
