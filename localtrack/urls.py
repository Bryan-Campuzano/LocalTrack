from django.contrib import admin
from django.urls import path
from analytics import views as analytics_views
from front import views as front_views
from human_resources import views as hr_views
from inventory import views as inventory_views
from sales import views as sales_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analytics/dashboard/', analytics_views.dashboard, name='dashboard'),
    path('analytics/reports/', analytics_views.reports, name='reports'),
    path('', front_views.home, name='front'),  # Asegúrate de que 'home' esté definido
    path('front/', front_views.login_view, name='login'),
    path('front/', front_views.register, name='register'),
    path('front/', front_views.home_view, name='home'),
    path('front/usr_profile', front_views.usr_profile, name='usr_profile'),
    path('human_resources/pqrs/', hr_views.pqrs_list, name='pqrs_list'),
    path('human_resources/pqrs/new/', hr_views.pqrs_new, name='pqrs_new'),
    path('human_resources/pqrs/edit/<int:id>/', hr_views.pqrs_edit, name='pqrs_edit'),
    path('human_resources/pqrs/delete/<int:id>/', hr_views.pqrs_delete, name='pqrs_delete'),
    path('inventory/products/', inventory_views.inventory_list, name='inventory_list'),
    path('inventory/products/new/', inventory_views.product_new, name='product_new'),
    path('inventory/products/edit/<int:id>/', inventory_views.product_edit, name='product_edit'),
    path('inventory/products/delete/<int:id>/', inventory_views.product_delete, name='product_delete'),
    path('sales/clients/', sales_views.clients_list, name='clients_list'),
    path('sales/clients/new/', sales_views.clients_new, name='clients_new'),
    path('sales/clients/edit/<int:id>/', sales_views.clients_edit, name='clients_edit'),
    path('sales/clients/delete/<int:id>/', sales_views.clients_delete, name='clients_delete'),
    path('sales/orders/', sales_views.orders_list, name='orders_list'),
    path('sales/orders/new/', sales_views.orders_new, name='orders_new'),
    path('sales/orders/edit/<int:id>/', sales_views.orders_edit, name='orders_edit'),
    path('sales/orders/delete/<int:id>/', sales_views.orders_delete, name='orders_delete'),
    path('users/profile/', user_views.profile, name='profile'),
    path('users/password/', user_views.password, name='password'),
    path('users/password_change/', user_views.password_change, name='password_change'),
]
