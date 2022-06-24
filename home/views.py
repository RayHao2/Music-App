from configparser import SectionProxy
from email.mime import audio
from operator import truediv
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import instrument, audio, rate
from .form import rateForm
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")




#class that handle json response from website(button click)
class PostJsonListView(View):
    def get(self, *args, **kwargs):
        # print(kwargs)
        #get two number from jsonrequest
        first = kwargs.get('first') 
        second = kwargs.get('second')
        #get audio object accrdoing to the variable pass in

        # firstAudio = list(audio.objects.values()[first:first+1])
        # secondAudio = list(audio.objects.values()[second:second+1])

        # firstAudio = serializers.serialize("json", audio.objects.filter(instrumentId=first).values())
        # secondAudio = serializers.serialize("json", audio.objects.filter(instrumentId=second).values())

        firstAudio = list(audio.objects.filter(instrumentId=first).values())
        secondAudio = list(audio.objects.filter(instrumentId=second).values())

        


        
        return JsonResponse({'firstAudio':firstAudio, 'secondAudio':secondAudio}, safe=False)


def survey(request):
        
    return render(request, "frontend/testView.html")



#a view that use to handle ajax submission
def submit(request):
    if request.method == 'POST':
        print("=== submit view recice submission")
        first = request.POST['first']
        second = request.POST['second']
        ids = request.POST['ids']
        print("=== first: " + first)
        print("=== second: " + second)
        print("=== selcted ids: " + ids)


    else:
        print(" === submit view didn't recice submission")
    return HttpResponse()


#NEED TO DO
#Pass in a form according to the instrument number 


#Note

#save with git

#git add .
#git commit -am 'message here'
#git push


