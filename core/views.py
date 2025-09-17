from django.shortcuts import render
from django.http import request, HttpResponse

# === Minhas Views === 

# Views de Registro
def register_view(request):
    return HttpResponse (" Views de Registro.")

# Views da Dashboard, aqui o usuario cria seus post's
def dashboard_view(request):
    return render(request, 'core/dashboard.html')

# Views Reels para mostrar todos os post's.
def reels_view(request):
    return HttpResponse (" View Reels")

# Views de Post
def post_view(request):
    return HttpResponse ("Essa é a views de cada Post feita!")

