from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from front.forms import UserRegistrationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia 'home' al nombre de la URL a la que deseas redirigir
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'users/login.html')

def home_view(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')  # Cambia 'login' al nombre de la URL que corresponde
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')  # Asegúrate de que 'home.html' exista en tu carpeta de plantillas.

