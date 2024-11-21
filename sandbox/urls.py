from django.urls import path
from .views import BruteForceView, SQLInjectionView, XSSView, CSRFView, DDOSView, DataLeakView

urlpatterns = [
    path('brute-force/', BruteForceView.as_view(), name='brute-force'),
    path('sql-injection/', SQLInjectionView.as_view(), name='sql-injection'),
    path('xss/', XSSView.as_view(), name='xss'),
    path('csrf/', CSRFView.as_view(), name='csrf'),
    path('ddos/', DDOSView.as_view(), name='ddos'),
    path('data-leak/<int:pk>/', DataLeakView.as_view(), name='data-leak'),
    path('sql-injection/', SQLInjectionView.as_view(), name='sql-injection'),
]
