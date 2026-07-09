from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sales(request):
    return render(request, 'sales.html')

def product(request):
    return render(request, 'product.html')

def product_create(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        p = Product(
            brand=brand,
            name=name,
            price=price,
            stock=stock
        )
        p.save()
        return redirect('list')
    
    return render(request, 'product/create.html')

def product_read(request, pk=None):
    if pk is None:
        return redirect('list')
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'product/read.html', {'product': p})

def product_update(request, pk=None):
    if pk is None:
        return redirect('list')
    p = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        p.brand = request.POST.get('brand')
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.stock = request.POST.get('stock')
        p.save()
        return redirect('list')
    return render(request, 'product/update.html', {'product': p})

def product_delete(request, pk=None):
    if pk is None:
        return redirect('list')
    p = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        p.delete()
        return redirect('list')
    return render(request, 'product/delete.html', {'product': p})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

def menu(request):
    return render(request,'menu.html')