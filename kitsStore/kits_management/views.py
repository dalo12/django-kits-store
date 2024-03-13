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
    if request.method == "POST":
        print(request)
        """new_kit = Kit(

        )
        new_kit.save()"""
    return render(request, "kits/add.html", {
        "talles_validos": TALLES_VALIDOS,
        "titulo": "Agregar nuevo kit",
        "teams": Team.objects.all(),
        "categories": Category.objects.all()
    })