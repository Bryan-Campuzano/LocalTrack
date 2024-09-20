from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('urs_profile/', views.urs_profile, name='profile'),
    path('password/new/', views.password_change, name='password_new'),
    path('password/', views.password, name='password'),
]
