from django.shortcuts import render

def dashboard(request):
    # Lógica para procesar los datos del dashboard
    return render(request, 'analytics/dashboard.html')  # Asegúrate de que esta plantilla exista

def reports(request):
    # Lógica para procesar los informes
    return render(request, 'analytics/reports.html')  # Asegúrate de que esta plantilla exista
