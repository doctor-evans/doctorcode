# Generated by Django 4.0.5 on 2022-07-01 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Admin', max_length=250)),
                ('title', models.CharField(default='Admin', max_length=250)),
                ('aboutAdmin', models.TextField()),
                ('who_are_we', models.TextField()),
                ('profilePic', models.ImageField(upload_to='images')),
                ('email', models.EmailField(default='gainwealth@mail.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True, default='', null=True)),
                ('facebook', models.URLField(blank=True, default='', null=True)),
                ('youtube', models.URLField(blank=True, default='', null=True)),
                ('instagram', models.URLField(blank=True, default='', null=True)),
                ('linkedin', models.URLField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('meta_description', models.CharField(blank=True, max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
