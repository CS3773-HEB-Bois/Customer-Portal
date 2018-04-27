from .models import Shopper, ShoppingCart


class ShoppingCartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'shopping_cart_id' not in request.session:
            if 'shopper_id' not in request.session:
                print("Creating")
                shopper = Shopper()
                shopper.save()
                shopper_id = shopper.id
            else:
                shopper_id = request.session['shopper_id']
            cart = ShoppingCart()
            cart.shopper_id = shopper_id
            cart.save()
            request.session['shopper_id'] = shopper_id
            request.session['shopping_cart_id'] = cart.id
        return self.get_response(request)
