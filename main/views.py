import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from .serializers import TeacherSerializer
from . import models
from rest_framework.response import Response
# Create your views here.

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]

@csrf_exempt
def teacher_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if email is None or password is None:
                return JsonResponse({'success': False, 'error': 'Email or password not provided'}, status=400)

            try:
                teacherData = models.Teacher.objects.get(email=email, password=password)
                return JsonResponse({'success': True})
            except ObjectDoesNotExist:
                return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Server error'}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Unsupported method'}, status=405)
