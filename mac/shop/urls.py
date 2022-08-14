from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='AboutUs'),
    path('contact/', contact, name='ContactUs'),
    path('tracker/', tracker, name='TrackerStatus'),
    path('search/', search, name='Search'),
    path('productview', productView, name='index'),
    path('checkout', checkout, name='index'),
]