from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]
