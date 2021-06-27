from django.shortcuts import render
from .models import ProductCategory, Product


def products(request, pk=None):
    print(pk)
    title = 'продукты/каталог'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request=request, template_name='mainapp/products.html', context=context)


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
