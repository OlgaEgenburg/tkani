from django.shortcuts import render, get_object_or_404
from .models import Category, Item, Subcategory
from cart.forms import CartAddProductForm
from django.views.generic import ListView

# Create your views here.
def list(request):
    return render(request, 'company/about.html')

def category_items(request, category_slug):
    """Create category template."""
    template = 'catalog/category.html'
    subcategory = get_object_or_404(
        Subcategory, slug=category_slug
    )
    item_list = Item.objects.select_related('subcategory').filter(
        subcategory__slug=category_slug)
    print(item_list)
    context = {
        'subcategory': subcategory,
        'item_list': item_list,
    }
    return render(request, template, context)

class CategoryListView(ListView):
    """Create index template."""

    model = Item
    template_name = 'catalog/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = Item.objects.select_related('subcategory').filter(subcategory__slug=kwargs)
        context['page_obg'] = post_list
        return context

def subcategory_items(request, category_slug):
    """Create category template."""
    template = 'catalog/subcategory.html'
    category = get_object_or_404(
        Category, slug=category_slug
    )
    subcategory_list = Subcategory.objects.select_related('category').filter(
        category__slug=category_slug)
    print(subcategory_list)
    context = {
        'category': category,
        'item_list': subcategory_list,
    }
    return render(request, template, context)

def item_detail(request, pk):
    template_name = 'catalog/item_detail.html'
    item = get_object_or_404(
        Item.objects.filter(is_published=True),
        pk=pk
    )
    cart_product_form = CartAddProductForm()
    context = {
        'item': item,
        'cart_product_form': cart_product_form
    }
    return render(request, template_name, context)
