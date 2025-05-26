from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('cartaopagina1/', views.cartaopagina1, name='cartaopagina1'),  # Página do cartão
    path('cartaopagina1/cartaopagina2/', views.cartaopagina2, name='cartaopagina2'),
    path('cartaopagina1/cartaopagina2/cartaopagina3/', views.cartaopagina3, name='cartaopagina3'),
]