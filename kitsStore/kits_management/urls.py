from django.urls import path
from . import views

urlpatterns = [
    path('', views.KitsList.as_view(template_name="kits/index.html"), name="index"),
    path('create', views.CreateKit.as_view(template_name="kits/create.html"), name="create")
]