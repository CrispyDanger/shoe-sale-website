import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from shopping.models import Product

from .models import Cart, CartItem


class CartListView(View):
    def get(self, request):
        current_user = request.user
        cart = Cart.objects.get_or_create(user=current_user)[0]
        cartItems = CartItem.objects.filter(cart=cart.id)

        context = {
            "cart_items": cartItems,
        }

        return render(request, "pages/cart.html", context)


class CartUpdateView(View):
    def post(self, request):
        data = json.loads(request.body)
        productId = data["productId"]
        action = data["action"]
        print("Action", action)
        print("ProductId", productId)

        current_user = request.user
        product = Product.objects.get(id=productId)

        cart = Cart.objects.get_or_create(user=current_user)

        cartItem = CartItem.objects.get_or_create(cart=cart.id, product=product)

        if action == "add":
            cartItem.quantity += 1
        elif action == "remove":
            cartItem.quantity -= 1

        cartItem.save()

        if cartItem.quantity <= 0:
            cartItem.quantity.delete()

        return JsonResponse("Item was added to cart", safe=False)


# Create your views here.
