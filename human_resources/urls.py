from django.urls import path
from . import views

app_name = 'human_resources'

urlpatterns = [
    path('pqrs/', views.pqrs_list, name='pqrs_list'),
    path('pqrs/new/', views.pqrs_new, name='pqrs_new'),
    path('pqrs/edit/<int:id>/', views.pqrs_edit, name='pqrs_edit'),
    path('pqrs/delete/<int:id>/', views.pqrs_delete, name='pqrs_delete'),
]
