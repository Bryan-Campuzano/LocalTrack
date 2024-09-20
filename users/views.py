# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # Puedes agregar lógica para mostrar y editar el perfil del usuario
    return render(request, 'users/profile.html')

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantiene al usuario autenticado
            return redirect('users:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password.html', {'form': form})

@login_required
def password(request):
    # Agrega lógica si deseas permitir a los usuarios establecer una nueva contraseña
    return render(request, 'users/password.html')
