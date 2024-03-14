from django.urls import path
from . import views

urlpatterns = [
    path('', views.KitsList.as_view(template_name="kits/index.html"), name="index"),
    path('add', views.add, name="add")
]