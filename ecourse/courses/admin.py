from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import mark_safe
from .models import Course, Category, Tag, User, Lesson
from django.contrib.auth.models import Permission, ContentType
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from . import dao

# Register your models here.
class CourseAdminSite(admin.AdminSite):
    site_header = "Hệ thống khoá học trực tuyến"

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats_view.html',{
            'stats': dao.count_course_by_cate()
        })

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk','name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class CourseForm(forms.ModelForm):
  description = forms.CharField(widget=CKEditorUploadingWidget)

  class Meta:
    model = Course
    fields = '__all__'

class TagStackedInline(admin.StackedInline):
    model = Course.tags.through
class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    readonly_fields = ['img']
    form = CourseForm
    inlines = [TagStackedInline]
    def img(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=obj.image.name)
            )
    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

admin_site = CourseAdminSite(name="myapp")

admin_site.register(Course, CourseAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag)
admin_site.register(Lesson)
admin_site.register(User)
admin_site.register(Permission)
admin_site.register(ContentType)