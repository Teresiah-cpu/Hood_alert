from django.contrib.auth import views 
from django.urls import path, include
from django.urls import path as url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('',include('hoodapp.urls')),
    
]