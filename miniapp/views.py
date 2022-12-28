from django.shortcuts import HttpResponse, render
from miniapp.models import Event


def childhood(request):
    objs = Event.objects.filter(category__title='childhood')
    if objs:
        return render(request, 'childhood.html', {'obj': objs})
    return HttpResponse('<h1>Not found</h1>', status=404)


def youth(request):
    objs = Event.objects.filter(category__title='youth')
    if objs:
        return render(request, 'youth.html', {'obj': objs})
    return HttpResponse('<h1>Not found</h1>', status=404)


def adulthood(request):
    objs = Event.objects.filter(category__title='adulthood')
    if objs:
        return render(request, 'adulthood.html', {'obj': objs})
    return HttpResponse('<h1>Not found</h1>', status=404)
