from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.list, name='list'),
    path('category/<slug:category_slug>/', views.category_items,
         name='category_items'),
    path('subcategory/<slug:category_slug>/', views.subcategory_items,
         name='subcategory_items'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
]
