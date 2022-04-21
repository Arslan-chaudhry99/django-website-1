from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    
    return render(request, "store/index.html")

def collections(request):
    category=Category.objects.filter(status=0)
    context={"category":category}
    return render(request, 'store/collections.html', context )

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
      products=Product.objects.filter(category__slug=slug)
      category_name=Category.objects.filter(slug=slug).first()
      contex={"products":products,"category_name":category_name}
      print(products)
      return render(request, "store/product/index.html", contex)
    else:
     return HttpResponse('This is not a valid product')
    

