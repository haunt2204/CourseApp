from django.db.models import Count

from .models import Category, Course, Tag, Lesson


def load_courses(params={}):
    q = Course.objects.all()
    kw = params.get('kw')
    if kw:
        q = q.filter(name__icontains=kw)

    cate = params.get('cate_id')
    if cate:
        q = q.filter(cate_id=cate)

def count_course_by_cate():
    return Category.objects.annotate(count=Count('courses__id')).values("id", "name", "count").order_by('id')