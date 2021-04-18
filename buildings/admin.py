from django.contrib import admin
from . models import Home, ImageFiles

# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'agent', 'slug', 'title', 'city', 'sale_type', 'home_type', 'price', 'bedrooms', 'bathrooms', 'sqft', 'photo', 'is_published']

@admin.register(ImageFiles)
class ImageFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'home']


