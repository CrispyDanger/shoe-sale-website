from .models import Category


def categories_fetcher(request):
    categories = Category.objects.all()
    return {
        "categories": categories,
    }
