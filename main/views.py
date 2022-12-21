from django.shortcuts import render
from .models import Items
from django.views.generic import DetailView

def index(request):
    data = {
        'title': 'Главная',
        'breadcrumbs': 'none'
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'О нас',
        'breadcrumbs': '',
        'authorname': 'Alex',
        'authorlastname': 'Biryukov',
        'authorphone': '8-999-777-66-55',
        'authormail': 'Alex@sobaka.com',
    }

    return render(request, 'main/about.html', data)


def catalog(request):
    items = Items.objects.order_by('-id')

    return render(request, 'main/catalog.html', {'items': items})


class ItemsDetail(DetailView):
    model = Items
    template_name = 'main/detail.html'
    context_object_name = 'item'