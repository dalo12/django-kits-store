from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Kit, Team

# Create your views here.
def index(request):
    return render(request, "kits/index.html", {
        "kits": Kit.objects.all()
    })