from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from .models import Category, Product


class CategoryListView(ListView):
    template_name = "base.html"
    model = Category


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()

        context = {"categories": categories, "products": products}

        return render(request, "pages/home.html", context)


class CategoryView(View):
    def get(self, request, slug):
        if slug == "all":
            products = Product.objects.all()
        else:
            category = get_object_or_404(Category, slug=slug)
            products = Product.objects.filter(category_id=category)

        context = {
            "products": products,
        }

        return render(request, "pages/category.html", context)


# Create your views here.
