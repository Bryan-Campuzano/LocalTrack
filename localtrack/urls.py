from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),  
    path('users/', include('users.urls')),
    path('analytics/', include('analytics.urls')),
    path('sales/', include('sales.urls')),
    path('inventory/', include('inventory.urls')),
    path('human_resources/', include('human_resources.urls')),
]
