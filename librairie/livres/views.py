from django.shortcuts import render
from livres.models import Livres
from .forms import Forms

def home(request):
    livres = Livres.objects.all()
    return render(request, 'index.html', context={'livres': livres})


def formulaire(request):
    forms = Forms(request.POST or None)
    if forms.is_valid():
        forms.save()
        forms = Forms()
        #messages = "Votre message a été envoyé avec succès :)"
    return render(request, 'formulaire.html', {'forms': forms})
