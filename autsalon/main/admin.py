from django.contrib import admin
from .models import Brand, Car


class Brandadmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_at')
    list_display_links = ('name',)
    search_fields = ('name', 'country')

admin.site.register(Brand, Brandadmin)


class Caradmin(admin.ModelAdmin):
    list_display = ('name', 'model_year', 'photo', 'price', 'brand')
    list_display_links = ('name',)
    search_fields = ('name', 'brand__name')
    list_max_show_all = 10
    list_per_page = 10

admin.site.register(Car, Caradmin)
