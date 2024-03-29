from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename="categories")
router.register('courses', views.CourseViewSet, basename="courses")
router.register('lessons', views.LessonViewSet, basename="lesson")
router.register('users', views.UserViewSet, basename="user")
router.register('comments', views.CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(router.urls)),
    path('courses/', views.list, name='list'),
    path('courses/<int:course_id>', views.details, name='detail'),
    path('category/', views.CategoryView.as_view()),
]