# from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path as url
from django.urls import path, include


urlpatterns=[
    path('',views.home,name = 'home'),
    path('details/(\d+)', views.details, name='details'),
    path('add/business/', views.addBusiness, name='business'),
    path('create/post/', views.addPost , name='post'),
    path('myprofile/', views.addProfile , name='profile'),
    path('add/health/', views.addHealth, name='health'),
    path('add/police_post/', views.addPolice, name='police'),
    path('business/(\d+)', views.business_details, name='business_details'),
    path('search/(\d+)', views.search_business, name='search_business')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)