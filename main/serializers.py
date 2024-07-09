from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['id','first_name', 'second_name', 'email', 'password', 'qualifications', 'mobile_no', 'skills', 'address']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseCategory
        fields=['id','tittle', 'description']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Course
        fields=['id','teacher', 'tittle','description','featured_img','techs']
