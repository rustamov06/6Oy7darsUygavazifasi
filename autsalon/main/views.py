from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand, Car
from .form import CarForm, BrandForm

def index(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    context = {
        'brands': brands,
        'cars': cars
    }
    return render(request, 'index.html', context)

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = Car.objects.filter(brand=brand)
    all_brands = Brand.objects.all()
    context = {
        'brand': brand,
        'cars': cars,
        'all_brands': all_brands
    }
    return render(request, 'brand_cars.html', context)

def brands_list(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'brands.html', context)

def cars_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars.html', context)

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {'car': car}
    return render(request, "car_detail.html", context)


def add_cars(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_cars')
    else:
        form = CarForm()
    return render(request, 'add_cars.html', {'form': form})

def add_brands(request):
    brands = Car.objects.all()
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_brand')
    else:
        form = BrandForm()
    context = {
        'form': form,
        'brands': brands
    }
    return render(request, 'add_brands.html', context)