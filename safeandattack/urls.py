
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/sandbox/', include('sandbox.urls')),  # Підключення маршрутів пісочниці
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/ads/', include('ads.urls')),
    
]