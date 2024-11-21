from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connections
from .models import VulnerableUser
from django.http import JsonResponse

class BruteForceView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        if username == "admin":
            return Response({"result": "Brute-force успішний: пароль 'admin123'"})
        return Response({"result": "Brute-force не вдався"}, status=status.HTTP_401_UNAUTHORIZED)

class SQLInjectionView(APIView):
    def post(self, request):
        query = request.data.get('query', '')
        try:
            # Виконання небезпечного SQL-запиту
            with connections['sandbox'].cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()  # Отримання результатів

            # Повернення результатів у JSON-форматі
            return JsonResponse({"result": f"SQL Injection успішний!\n\n{result}", "data": result})
        except Exception as e:
            return JsonResponse({"result": f"Помилка SQL: {str(e)}"}, status=400)
class XSSView(APIView):
    def post(self, request):
        script = request.data.get('input', '')
        return Response({"result": f"Виконано XSS скрипт: {script}"})

class CSRFView(APIView):
    def post(self, request):
        action = request.data.get('action', '')
        return Response({"result": f"CSRF успішний: виконано дію {action}"})

class DDOSView(APIView):
    def post(self, request):
        count = int(request.data.get('count', 0))
        return Response({"result": f"Імітовано {count} DDoS запитів"})

class DataLeakView(APIView):
    def get(self, request, pk):
        return Response({"result": f"Дані з витоку для ID {pk}: [конфіденційні дані]"})
