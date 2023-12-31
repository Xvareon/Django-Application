from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductCreationForm, ProductUpdateForm
from .models import Product

# Create your views here.


def index(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query).order_by('id')
    else:
        products = Product.objects.all().order_by('id')

    return render(request, "products-index.html", {'products': products})


def create(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductCreationForm()

    return render(request, "products-create.html", {'form': form})


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductUpdateForm(instance=product)

    return render(request, "products-update.html", {'form': form, 'product': product})


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('index')

    return redirect('index')


def view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products-view.html", {'product': product})
