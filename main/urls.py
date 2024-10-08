from django.urls import path
from . import views
# from .views import add_course

urlpatterns = [
    #Teacher
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login',views.teacher_login),

    #CourseCategory
    path('category/', views.CategoryList.as_view()),
    #course
    path('course/', views.CourseList.as_view()),
    #chapter
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),

      #chapter
    path('chapter/', views.ChapterList.as_view()),

    #Specific Course Chapter
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),

    #path('course/', add_course, name='add_course'),
    #TeacherCourses
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),

    #Teacher Specific Course
    path('teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),


] 