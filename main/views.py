import json
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from .serializers import CategorySerializer, CourseSerializer, TeacherSerializer, ChapterSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
                return JsonResponse({'success': True, 'teacher_id':teacherData.id})
            except ObjectDoesNotExist:
                return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Server error'}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Unsupported method'}, status=405)
    
        
class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer
    # permission_classes=[permissions.IsAuthenticated]

#course
class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes=[permissions.IsAuthenticated]


    #specific Teacher course
class TeacherCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        teacher=models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)

    #permission_classes=[permissions.IsAuthenticated]

# @api_view(['POST'])
# def add_course(request):
#     if request.method == 'POST':
#         print(request.data)  # Log request data for debugging
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(serializer.errors)  # Log serializer errors for debugging
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#chapter
class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer
    #permission_classes=[permissions.IsAuthenticated]
