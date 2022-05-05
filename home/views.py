from email.mime import audio
from operator import truediv
from re import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import instrument, audio, rate
from .form import rateForm
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")



def survey(request):
    #create an instance capture user selection on audio

    #create two object of rate field 
    
    #the one where user selected should be rate =1, other one is rate =0

    #save the rate object 
    choosen = request.POST.get('ids')
    print(choosen)
    return render(request, "frontend/testView.html")

#class that handle json response from website(button click)
class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        #get two number from jsonrequest
        first = kwargs.get('first') 
        second = kwargs.get('second')
        #get audio object accrdoing to the variable pass in

        firstAudio = list(audio.objects.values()[first:first+1])
        secondAudio = list(audio.objects.values()[second:second+1])
        
        return JsonResponse({'firstAudio':firstAudio, 'secondAudio':secondAudio}, safe=False)





#NEED TO DO
#Pass in a form according to the instrument number 


#Note

#save with git

#git add .
#git commit -am 'message here'
#git push


