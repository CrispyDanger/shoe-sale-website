from .models import Cart, CartItem


def cart_items_fetch(request):
    current_user = request.user
    user_cart = Cart.objects.get_or_create(user=current_user)
    cartItem_query = CartItem.objects.filter(cart=user_cart[0])
    cartItem_quantity = sum([cartItem.quantity for cartItem in cartItem_query])
    return {
        "cart_quantity": cartItem_quantity,
    }
