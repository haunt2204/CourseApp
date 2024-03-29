from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Course, Lesson, User, Comment, Like
from rest_framework import viewsets, generics, status, permissions
from rest_framework.parsers import MultiPartParser
from . import serializer, paginator, perms

# Create your views here.
class CategoryView(View):
    def get(self, request):
        cates = Category.objects.all()
        return render(request, 'courses/list.html',
                      {'categories': cates})
    def post(self, request):
        pass
def index(request):
    return HttpResponse("<h1>Hello CS2001</h1>")

def list(request):
    return HttpResponse("<h1>COURSES LIST</h1>")

def details(request, course_id):
    return HttpResponse(f"{course_id}")

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer

class CourseViewSet(viewsets.ViewSet,generics.ListAPIView, generics.CreateAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializer.CourseSerializer
    pagination_class = paginator.PaginatorCourse

    def get_queryset(self):#Loc theo q
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['get'], detail=True)#Bai 3
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True).all()
        q = request.query_params.get("q")
        if q:
            lessons = lessons.filter(name__icontains=q)
        return Response(serializer.LessonSerializer(lessons, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = serializer.LessonSerializerDetail
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['add_comment', 'like']:
            return [permissions.IsAuthenticated()]
        return self.permission_classes

    @action(methods=['post'], url_path='comments', detail=True)
    def add_comment(self, request, pk):
        c = Comment.objects.create(user=request.user,lesson=self.get_object(), content = request.data.get('content'))
        return Response(serializer.CommentSerializer(c).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path='like', detail=True)
    def like(self,request,pk):
        like, created = Like.objects.get_or_create(user=request.user, lesson=self.get_object())
        if not created:
            like.active = not like.active
            like.save()

        return Response(serializer.LessonSerializerDetail(self.get_object(), context={
            'request': request
        }).data, status=status.HTTP_200_OK)
class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializer.CommentSerializer
    permission_classes = [perms.OwnerPermission]

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
    parser_classes = [MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated]

        return [permissions.AllowAny]

    #user/current_user/
    @action(methods=['get'], url_name='current', detail=False)
    def current_user(self, request):
        return Response(serializer.UserSerializer(request.user).data)