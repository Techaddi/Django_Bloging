from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index', views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('post', views.post, name='post'),
    path('<str:title>',views.blogpost, name='blogpost')
    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)