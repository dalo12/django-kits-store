from django.contrib import admin
from .models import Category, Kit, Team

# Register your models here.
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Kit)
