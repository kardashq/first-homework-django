from django.urls import path
from miniapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('childhood/', childhood, name='childhood'),
    path('youth/', youth, name='youth'),
    path('adulthood/', adulthood, name='adulthood'),
]
