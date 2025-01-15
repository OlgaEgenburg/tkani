from catalog.models import Category
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
class IndexListView(ListView):
    model = Category
    ordering = 'id'
    template_name = 'home/index.html'

def index_list(request):
    # Получаем список всех объектов с сортировкой по id.
    category = Category.objects.order_by('id')
    # Создаём объект пагинатора с количеством 10 записей на страницу.
    context = {'page_obj': category}
    return render(request, 'home/index.html', context) 
