# Generated by Django 5.0.3 on 2024-03-08 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='courses/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='course',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='courses.category'),
        ),
    ]
