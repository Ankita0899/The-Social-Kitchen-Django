from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('gallery', views.gallery, name='gallery'),
    path('catering', views.catering, name='catering'),
    path('work', views.work, name='work'),
    path('contact', views.contact, name='contact'),

]