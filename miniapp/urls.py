from django.urls import path
from miniapp.views import childhood, youth, adulthood

urlpatterns = [
    path('childhood/', childhood),
    path('youth/', youth),
    path('adulthood/', adulthood),
]
