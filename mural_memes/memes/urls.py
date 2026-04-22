from django.urls import path
from . import views

app_name = 'memes'

urlpatterns = [
    path('',          views.lista_memes,  name='lista'),
    path('<int:pk>/', views.detalhe_meme, name='detalhe'),
    path('enviar/',   views.enviar_meme,  name='enviar'),
]
