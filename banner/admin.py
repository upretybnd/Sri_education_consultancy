from django.contrib import admin

# Register your models here.
# banner/admin.py
from django.contrib import admin
from .models import CarouselItem, Country


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ('active',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)