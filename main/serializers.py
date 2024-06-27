from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['id','first_name', 'second_name', 'email', 'password', 'qualifications', 'mobile_no', 'skills', 'address']
        