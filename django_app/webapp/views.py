from django.shortcuts import render, redirect
from .forms import ProductCreationForm
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})


def create(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductCreationForm()

    return render(request, "create.html", {'form': form})
