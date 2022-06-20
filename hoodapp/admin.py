# from django.apps import AppConfig


# class ViciniaConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'hoodapp'
from django.contrib import admin
from .models import Profile,Post,Health ,Police,NeighbourHood,Business
# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Police)
admin.site.register(Health)