from .models import Shopper, ShoppingCart, RegisteredShopper


class ShoppingCartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'shopping_cart_id' not in request.session:
            if 'shopper_id' not in request.session:
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


class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'shopper_id' in request.session:
            shopper = RegisteredShopper.objects.filter(
                id=request.session['shopper_id']).first()
            if shopper:
                request.session['shopper_info'] = {
                    'first_name': shopper.first_name,
                    'last_name': shopper.last_name
                }
        return self.get_response(request)
