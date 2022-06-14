from django.shortcuts import render
from django.http import HttpResponse
import logging

from . models import Product 
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def index(request):
    return render(request, 'base.html')

def search(request):
    query = request.GET["query"]
    products = Product.objects.filter(name__contains=query)
    return render(request, 'pages/search_result.html', 
                        {"query":query, "products":products})

def product(request, pcces_encode):
    product = Product.objects.get(pcces_encode=pcces_encode)
    if product.review_date == None: 
        product.review_date = ''
    product.create_date = product.create_date.strftime("%m/%d/%Y")
    return render(request, 'pages/product.html', 
                        {"product":product})
