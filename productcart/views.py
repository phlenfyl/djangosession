from django.shortcuts import render


from base.views import G
from .models import *
from .cart import Cart

# Create your views here.


def checkout(request):
    itemtotal = 0
    count = 0
    prod = Cart(request)

    

    return render(request, 'utils/checkout.html', {'prod':prod, 'count':count, 'itemtotal':itemtotal})




            # $('#decrementBtn').click(function (e) {
            #    e.preventDefault()
            #     //updateQuantity(-1)
            #     var quantityInput = $('#quantityInput');
            #     // Decrease the value by 1, but ensure it doesn't go below 0
            #     quantityInput.val(Math.max(1, parseInt(quantityInput.val()) - 1));
            # });

            # $('#incrementBtn').click(function (e) {
            #     e.preventDefault()
            #     //updateQuantity(1)
            #     var quantityInput = $('#quantityInput');
            #     // Increase the value by 1
            #     quantityInput.val(parseInt(quantityInput.val()) + 1);
            # });

        # });
        # $(document).ready(function(){
        #     $('#decrementBtn, #incrementBtn').click (function(e){
        #         e.preventDefault();
        #         var quantityInput = $('#quantityInput');
        #         var change = $(this).attr('id') === 'decrementBtn' ? -1 : 1;
        #         quantityInput.val(Math.max(1, parseInt(quantityInput.val()) + change));

        #         $.ajax({
        #             type: 'POST',
        #             url: '{% url "commerce:updatecart" %}',
        #             data: {
        #                 post_id: $('#prod_id').val(),
        #                 qty_update: quantityInput.val(),,
        #                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        #                 action: 'post'
        #             },
        #             success: function(response){
        #             console.log(response.status)
        #             },
        #             error: function(rs, e){
        #             console.log(rs.responseText);
        #             },
        #         });
        #     });

        #         function updateQuantity(change) {
        #     var quantityInput = $('#quantityInput');
        #     var newValue = Math.max(1, parseInt(quantityInput.val()) + change);
        #     quantityInput.val(newValue);

        #     // Send the updated value to Django backend using Ajax
        #     $.ajax({
        #         method: 'POST',
        #         url: '{% url "commerce:cartupdate" %}',
        #         data: {
        #             prod_id: $('#prod_id').val(),
        #             qty_update: newValue,
        #             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        #         },
        #         success: function (response) {
        #             // Handle the success response from the server if needed
        #             console.log(response.status)
        #         },
        #         error: function (error) {
        #             // Handle errors if any
        #             console.error('Error updating value:', error);
        #         }
        #     });
        # }



