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

class KitsList(ListView):
    model = Kit

class CreateKit(SuccessMessageMixin, CreateView):
    model = Kit
    form = Kit
    fields = "__all__"
    success_message = "Kit creado correctamente"
    extra_context = {
        "talles_validos" : ['XS','S','M','L','XL','XXL','XXXL','XXXXL','XXXXXL'],
        "categories" : Category.objects.all(),
        "teams" : Team.objects.all()
    }

    def get_success_url(self):
        return reverse('index')

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
        messages.success (self.request, (success_message))
        return reverse('index')