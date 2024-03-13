from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Kit, Team

# Instanciar las vistas genéricas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

TALLES_VALIDOS = ['XS','S','M','L','XL','XXL','XXXL','XXXXL','XXXXXL'];

class KitsList(ListView):
    model = Kit

class CreateKit(SuccessMessageMixin, CreateView):
    model = Kit
    form = Kit
    fields = "__all__"
    success_message = "Kit creado correctamente"

    def get_success_url(self):
        return reverse('index')

class KitDetail(DetailView):
    model = Kit

class UpdateKit(SuccessMessageMixin, UpdateView):
    model = Kit
    form = Kit
    fields = "__all__"
    success_message = "Kit actualizado correctamente"

    def get_success_url(self):
        return reverse('index')

class DeleteKit(SuccessMessageMixin, DeleteView):
    model = Kit
    form = Kit
    fields = "__all__"

    def get_success_url(self):
        success_message = "Kit eliminado correctamente"
        message.success (self.request, (success_message))
        return reverse('index')

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