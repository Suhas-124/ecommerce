from django.shortcuts import render
from product.models import Product

def home_view(request):
    products=Product.objects.all().filter(is_available=True)
    return render(request,'home.html',{'products':products})
