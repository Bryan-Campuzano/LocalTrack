from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/edit/<int:id>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),
]
