# Generated by Django 3.2.6 on 2022-06-19 16:31

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
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
                ('population', models.IntegerField()),
                ('description', models.TextField()),
                ('area_pic_one', models.ImageField(blank=True, null=True, upload_to='neighbourhood_pics/')),
                ('area_pic_two', models.ImageField(blank=True, null=True, upload_to='neighbourhood_pics/')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'neighbourhood',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('why_here', models.TextField(blank=True, max_length=200, null=True, verbose_name='What do you like about the above neighbourhood?')),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('post_pic', models.ImageField(blank=True, null=True, upload_to='post_pic/')),
                ('contacts', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='police_pic/')),
                ('contacts', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'police',
            },
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='health_pic/')),
                ('contacts', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'health',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('business_pic_one', models.ImageField(blank=True, null=True, upload_to='business_pics/')),
                ('business_pic_two', models.ImageField(blank=True, null=True, upload_to='business_pics/')),
                ('Phone_no', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('products', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'business',
            },
        ),
    ]
