from django.shortcuts import render
from banner.models import CarouselItem, Country


def home(request):
    carousel_items = CarouselItem.objects.filter(active=True)  # Fetch active carousel items
    countries = Country.objects.all()  # Fetch all countries from the database
    return render(request, 'home.html', {
        'carousel_items': carousel_items,
        'countries': countries,
    })


def contact_us(request):
    return render(request, 'contact_us.html')


def ielts(request):
    return render(request, 'ielts.html')


def pte(request):
    return render(request, 'pte.html')


def about_us(request):
    countries = Country.objects.all()
    return render(request, 'about_us.html', {
        'countries': countries,
    })
