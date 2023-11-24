from django.shortcuts import render, get_object_or_404



from commerce.models import *
from productcart.models import *
from dataclasses import dataclass

@dataclass
class G:
    prod = Product.objects.all()
    cat = Category.objects.all()
    cart = ProductCart.objects.all()


def index(request,category_slug= None):
    product = G.prod
    cateogry = None

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        product = G.prod.filter(category=category)[:5]

    return render(request, 'pages/index.html', {"product":product})

def about(request):
    
    return render(request, 'pages/aboutus.html')

def contact(request):
    
    return render(request, 'pages/contact.html')
