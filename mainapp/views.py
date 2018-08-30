from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404
import json, os

with open('static/new_products.json', 'r', encoding='UTF-8') as p:
    new_products_json = p.read()
    new_products = json.JSONDecoder().decode(new_products_json)

links_menu = [
    {'href': 'main', 'name':'home'},
    {'href': 'faq', 'name':'faq'},
    {'href': 'sale', 'name':'sale items'},
]

# def category_to_menu_dict (c):
#     return {'href': c, 'name': c}

# menu_category_start = 1
# for category in ProductCategory.objects.all():
#     links_menu.insert(menu_category_start, category_to_menu_dict(category.name.lower()))
#     menu_category_start+=1

content = {
    'products': Product.objects.all(),
    'links_menu': links_menu,
    'title': 'rubernLaces',
}

print(links_menu)
print("****************")
print(content)

# mens_content = {
#     'links_menu' : links_menu,
#     'title': 'mens',
#     'products' : Product.objects.all().filter(category__name='Mens'),
# }

# womans_content = {
#     'links_menu' : links_menu,
#     'title': 'womens',
#     'products' : Product.objects.all().filter(category__name='Womens'),
# }

# Create your views here.

def test(request, category):
    print(category)
    return HttpResponse("This is the test")

def index(request):
    return HttpResponse("Hello, this is mainapp index")

def main(request):
   return render(request, 'mainapp/index.html', content)
    
def checkout(request):
    return render(request, 'mainapp/checkout.html', content)
    
# def mens(request):
#     return render(request, 'mainapp/products.html', mens_content)

def products(request, category=None):
    print(category)
    title = 'All products'

        # if category == ''
        
    return render(request, 'mainapp/products.html', content)

# def womens(request):
#     return render(request, 'mainapp/products.html', womans_content)
    
def new(request):
    return render(request, 'mainapp/new.html', content)
    
def product(request):
    return render(request, 'mainapp/product.html', content)
    
def sale(request):
    return render(request, 'mainapp/sale.html', content)
    
def faq(request):
    return render(request, 'mainapp/faq.html', content)

def login(request):
    return render(request, 'mainapp/login.html', content)
    
