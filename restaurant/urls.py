from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('cartaopagina1/', views.cartaopagina1, name='cartaopagina1'),  # Página do cartão
]