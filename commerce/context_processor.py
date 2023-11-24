from productcart.cart import Cart
from base.views import G


def cartpros(request):
    return {'cart': Cart(request)}



def catnav(request):
    catlist = G.cat

    return {'catlist': catlist}
