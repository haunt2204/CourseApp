# Generated by Django 5.0.3 on 2024-03-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_course_image_alter_lesson_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(null=True, upload_to='lessons/%Y/%m'),
        ),
    ]
