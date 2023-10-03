from django.shortcuts import render, redirect
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        variant = request.POST.get('variant')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Product.objects.create(
            name=name,
            variant=variant,
            qty=qty,
            price=price,
            description=description
        )

        return redirect('index')

    return render(request, "create.html")
