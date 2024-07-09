from django.db import models

# Create your models here.
# Teacher Model
class Teacher(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualifications=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    skills=models.TextField()
    address=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="1. Teachers"


# Course Category Model
class CourseCategory(models.Model):
    tittle=models.CharField(max_length=150)
    description=models.TextField(max_length=100)

    class Meta:
        verbose_name_plural="2. Course Categories"

    def __str__(self):
        return self.tittle


# Course Model
class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tittle=models.CharField(max_length=150)
    description=models.TextField()
    featured_img = models.ImageField(upload_to='course_imgs/', null=True)
    techs=models.TextField(null=True)

    class Meta:
        verbose_name_plural="3. Courses"


# Student Model
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualifications=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    address=models.TextField()
    interested_categories=models.TextField()

    class Meta:
        verbose_name_plural="4. Students"