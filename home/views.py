from email.mime import audio
from operator import truediv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import instrument
from .models import audio
from .models import rate
from .form import rateForm
# Create your views here.
def index(request):
    return render(request, "frontend/index.html")



def survey(request):
    if request.method == 'POST':
        form = rateForm(request.POST)
        if form.is_valid():
            form.save()

    form = rateForm()
    wavFile = audio.objects.all()
    return render(request, "frontend/audio.html",{
        'wavFile': wavFile,
        'form': form,
    })

#Taks List
#1. auto generate rate object when instrument object is created 
#2. should rates be array


#save with git

#git add .
#git commit -am 'message here'
    
