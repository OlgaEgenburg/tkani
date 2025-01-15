from django.urls import path

from . import views

app_name = 'company'

urlpatterns = [
    path('', views.about, name='about'),
    path('list/', views.delivery, name='delivery'),
    path('sewing/', views.sewing, name='sewing'),
]
