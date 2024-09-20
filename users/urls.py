from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('password/', views.password_change, name='password_change'),
    path('password/new/', views.password_new, name='password_new'),
]
