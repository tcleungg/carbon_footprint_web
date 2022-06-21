from django.shortcuts import render
from django.http import HttpResponseRedirect
import logging

from . models import Product, PrimaryCategory, IndustrialCategory, \
                    AnalyticMethod, DataQuality, Co2Allocation, PccesEncode
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

def slice_pcces_encode(pcces_encode):
    return [pcces_encode[0], pcces_encode[1:6], pcces_encode[6],pcces_encode[7],pcces_encode[8],pcces_encode[9],pcces_encode[10]]

def product(request, pcces_encode):
    product = Product.objects.select_related().get(pcces_encode=pcces_encode)
    pcces_encode_desc = PccesEncode.objects.get(pcces_encode=pcces_encode)
    pcces_encode = slice_pcces_encode(pcces_encode)
    if product.review_date == None: 
        product.review_date = ''
    product.create_date = product.create_date.strftime("%m/%d/%Y")
    return render(request, 'pages/product.html', 
                            {"product":product, 
                            "pcces_encode":pcces_encode, 
                            "pcces_encode_desc":pcces_encode_desc})

def category(request):
    categories = PrimaryCategory.objects.all().prefetch_related('industrial_categories')
    for category in categories:
        category.category_id = category.category_id.strip()
    return render(request, 'pages/category.html', {"categories":categories})

def primary_category_products(request, primary_category):
    try:
        products = Product.objects.select_related('primary_category').filter(primary_category__name=primary_category)
    except Product.DoesNotExist:
        products = {}
    return render(request, 'pages/category_products.html', 
                            {"primary_category":primary_category, "products":products})

def industrial_category_products(request, primary_category, industrial_category):
    try:
        products = Product.objects.select_related('primary_category') \
                    .filter(primary_category__name=primary_category) \
                    .select_related('industrial_category').filter(industrial_category__name=industrial_category)
    except Product.DoesNotExist:
        products = {}
    return render(request, 'pages/category_products.html', 
                            {"primary_category":primary_category,
                                "industrial_category":industrial_category,
                                "products":products})
