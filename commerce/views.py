from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
import uuid

from productcart.models import *
from base.views import G
from .models import *
from productcart.cart import Cart




def categoryList(request, tag_slug=None):
    tag = None

    cats = Paginator(G.cat, 2)
    page_number =request.GET.get('page',all)
    catlist = cats.get_page(page_number)

    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        catlist = G.prod.filter(tags__in=[tag])

    return render(request, 'pages/category.html',{'catlist':catlist})

def prouctList(request, category_slug= None, tag_slug=None):
    prod = G.cart.filter(item_paid = False)
    cateogry = None
    tag = None

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        prodlist = G.prod.filter(category=category)

    prod= Paginator(prodlist, 2)
    page_num = request.GET.get('page', all)
    prodlist = prod.get_page(page_num)


    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        prodlist = G.prod.filter(tag=tag)

    return render(request, 'pages/product.html', {'prodlist':prodlist, 'prod':prod})


def prodDetails(request, slug):
    prod = get_object_or_404(Product, slug=slug)
    
    
    return render(request, 'pages/detail.html', {'prod':prod})


def addtocart(request):
    url = request.META.get('HTTP_REFERER')
    # prodcode = uuid.uuid4()
    cart = Cart(request)
    if request.method == "POST":
        if request.POST.get('cart') == 'cart':
        
            addQuan = int(request.POST['quantity'])
            add_id = int(request.POST["prodids"])

            prod_id = G.prod.get(pk= add_id)

            cart.add(prod_id=prod_id, qnt = addQuan)



            return redirect(url)
        elif request.POST.get('action') == 'post':
            new_qnt = int(request.POST.get('qty_new'))
            add_id = int(request.POST.get("prod_id"))

            prod_id = G.prod.get(pk= add_id)

            cart.add(prod_id=prod_id, qnt = new_qnt)

            return JsonResponse({'qnt': new_qnt})
        else:
            return JsonResponse({'status': 'Invalid request'}, status=400) 



def cart(request):
    subtotal = 0
    cart = Cart(request)
    
    if cart:
        subtotal += cart.get_total_price () 
    
    return render(request, 'utils/cart.html', {'cart':cart, 'subtotal':subtotal})



def updatecart(request):
    url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    subtotal = 0
    if request.POST.get('action') == 'post':
        update_qnt = int(request.POST.get('qty_update'))
        prod_id = int(request.POST.get('post_id'))
        cart.update(prod_id = prod_id, qnt = update_qnt)

        cartqnt = cart.__len__()
        cartsub = cart.get_total_price()

        if cart:
            subtotal += cart.get_total_price () 

        return JsonResponse ({'qnt': cartqnt, 'cartsub':cartsub, 'subtotal':subtotal})
    return redirect(url)

def remove_item(request):
    cart = Cart(request)
    url = request.META.get('HTTP_REFERER')
    # if the item in the cart is just a beat
    delprod = int(request.POST['deletecart'])
    cart.delete(prod_id=delprod)

    return redirect (url)


# npx tailwindcss -i ./base/static/src/input.css -o ./base/static/src/output.css --watch