from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Kit, Team

TALLES_VALIDOS = ['XS','S','M','L','XL','XXL','XXXL','XXXXL','XXXXXL'];

# Create your views here.
def index(request):
    return render(request, "kits/index.html", {
        "kits": Kit.objects.all(),
        "titulo": "Kits"
    })

def add(request):
    return render(request, "kits/add.html", {
        "talles_validos": TALLES_VALIDOS,
        "titulo": "Agregar nuevo kit"
    })