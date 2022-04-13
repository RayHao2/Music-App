from email.mime import audio
from operator import truediv
from re import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import instrument, audio, rate
from .form import rateForm
from django.views.generic import View, TemplateView
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")



def survey(request):
    if request.method == 'POST': #if something is post to the server, reference to HTML form method == post
        form = rateForm(request.POST)
        if form.is_valid():
            form.save()

    form = rateForm()
    wavFile = audio.objects.all()
    return render(request, "frontend/audio.html",{
        'wavFile': wavFile,
        'form': form,
    })

#class that handle json response from website(button click)
class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        #upper is to get the number from the js file to set a upper boundry
        upper = kwargs.get('num_aduios') #intial state be 3
        lower = upper - 3
        #pass in the audio in to the list [lower:upper] use to set boundry
        audios = list(audio.objects.values()[lower:upper]) 
        
        #comfirmation of no more audi to load
        audio_size = len(audio.objects.values())
        size = True if upper >= audio_size else False
        return JsonResponse({'data':audios, 'max': size}, safe=False)


class testView(TemplateView):
    template_name = 'frontend/testView.html'




#NEED TO DO
#how to pass only 2 audio in some sort of sequence?
    """
    1. OR use a button to cap the next and use python to manage the id
        -use ajax and json response to capture if the button got click
    """
#how to create form accoding to selection?


#Note

#save with git

#git add .
#git commit -am 'message here'
#git push
