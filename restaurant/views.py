from django.shortcuts import render
from django.views.generic import TemplateView

class restaurantView(TemplateView):
    template_name = 'restaurant/pages/'

def index(request):
    return render(request, 'pages/index.html')

def cartaopagina1(request):
    return render(request, 'pages/cartaopagina1.html')