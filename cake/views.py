from django.shortcuts import render
from .models import Cake


# Create your views here.

def index(request):
    cakes = Cake.objects.all()
    return render(request, 'index.html', {'cakes': cakes})


def about(request):
    return render(request, 'about.html', {})
