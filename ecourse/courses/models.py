from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField



# Create your models here.

class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=True)

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ['id']

class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.name

class Course(BaseModel):
    name = models.CharField(max_length=50, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to="courses/%Y/%m", null = True)
    category = models.ForeignKey(Category,related_name="courses", on_delete=models.RESTRICT, null=True)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.name

    # class Meta:
    #     unique_together = ('name', 'category')

class Lesson(BaseModel):
    name = models.CharField(max_length=50, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to="lesson/%Y/%m", null=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, null=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name
class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ineteraction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT, null=False)

    class Meta:
        abstract = True

class Comment(Ineteraction):
    content = models.CharField(max_length=255, null=False)

class Like(Ineteraction):
    active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'lesson')

class Rating(Ineteraction):
    rate = models.SmallIntegerField(default=0)
