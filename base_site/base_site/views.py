from django.shortcuts import render
from mainapp.models import Product


def index(request):
    title = 'магазин'

    products = Product.objects.all()[:8]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'base_site/index.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'base_site/contact.html', context=context)
