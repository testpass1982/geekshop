from django.shortcuts import render
from django.http import HttpResponse
import json, os

with open('static/new_products.json', 'r', encoding='UTF-8') as p:
    new_products_json = p.read()
    new_products = json.JSONDecoder().decode(new_products_json)

links_menu = [
    {'href': 'main', 'name':'home'},
    {'href': 'mens', 'name':'mens'},
    {'href': 'womens', 'name':'womens'},
    {'href': 'faq', 'name':'faq'},
    {'href': 'sale', 'name':'sale items'},
]

content = {
    'links_menu': links_menu,
    'title': 'rubernLaces',
    'new_products': new_products,
}

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is mainapp index")

def main(request):
    return render(request, 'mainapp/index.html', content)
    
def checkout(request):
    return render(request, 'mainapp/checkout.html', content)
    
def mens(request):
    return render(request, 'mainapp/mens.html', content)
    
def womens(request):
    return render(request, 'mainapp/womens.html', content)
    
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
    
