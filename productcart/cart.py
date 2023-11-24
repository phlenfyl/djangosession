from decimal import Decimal

from commerce.models import *
from productcart.models import *
from base.views import G


class Cart():



    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cartkey')
        if 'cartkey' not in request.session:
            cart = self.session['cartkey'] = {}
        
        self.cart = cart

    def add(self, prod_id, qnt):
        product_id = str(prod_id.pk)

        if product_id in self.cart:
            self.cart[product_id]['qnt'] = qnt
        else:
            self.cart[product_id] = {'price': str(prod_id.price), 'qnt':qnt}     
        self.save()

    def __iter__(self):
        prod_ids = self.cart.keys()
        products = G.prod.filter(pk__in = prod_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qnt']
            yield item

    

    def __len__(self):

        return sum(item['qnt'] for item in self.cart.values())

    
    def update(self, prod_id, qnt):

        product_id = str(prod_id)
        if product_id in self.cart:
            self.cart[product_id]['qnt'] = qnt  

        self.save()    

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qnt'] for item in self.cart.values())
    
    def delete(self, prod_id):
        product_id = str(prod_id)
        if product_id in self.cart:
            del self.cart[product_id]
            print(product_id)
            self.save()
        
    def save(self):
        self.session.modified = True


