from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "shop/product/list.html/",
        {"categories": categories, "products": products, "category": category},
    )
def product_detail(request, id, slug):
    # Get the get_absolute_url() of a model instance returns the URL that you would
    # use to reverse a detail view for that object with its primary key.
    product = get_object_or_404(Product, id=id, slug=slug, available=True)  # this is how we can protect against url manipulation
    cart_product_form = CartAddProductForm()
   
    return render( request, "shop/product/detail.html", { "product": product, 'cart_product_form': cart_product_form })