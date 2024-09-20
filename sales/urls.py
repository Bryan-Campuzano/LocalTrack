from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('clients/', views.clients_list, name='clients_list'),
    path('clients/new/', views.clients_new, name='clients_new'),
    path('clients/edit/<int:id>/', views.clients_edit, name='clients_edit'),
    path('clients/delete/<int:id>/', views.clients_delete, name='clients_delete'),
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/new/', views.orders_new, name='orders_new'),
    path('orders/edit/<int:id>/', views.orders_edit, name='orders_edit'),
    path('orders/delete/<int:id>/', views.orders_delete, name='orders_delete'),
]
