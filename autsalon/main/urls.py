from django.urls import path
from .views import index, brand_detail, car_detail, brands_list, cars_list, add_cars, add_brands, update_car, update_brand

urlpatterns = [
    path('', index, name='index'),
    path('brands/', brands_list, name='brands'),
    path('cars/', cars_list, name='cars'),
    path('brand/<int:brand_id>/', brand_detail, name='brand_detail'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
    path('add_cars', add_cars, name='add_cars'),
    path('add_brand/', add_brands, name='add_brand'),
    path('cars/update/<int:car_id>/', update_car, name='update_car'),
    path('brand/update/<int:brand_id>/', update_brand, name='update_brand'),
]
