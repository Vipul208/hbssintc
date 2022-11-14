from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('ad_process', views.ad_process, name='ad_process'),
    path('admission', views.admission, name='admission'),
    path('admissions', views.admissions, name='admissions'),
    path('contact', views.contact, name='contact'),
    path('notice', views.notice, name='notice'),
    path('teachers', views.teachers, name='teachers'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('gallery', views.gallery, name='gallery'),
    path('maintenance',views.maintenance, name='maintenance'),
    path('logout',views.logout, name='logout'),
    path('contacts',views.contacts, name='contacts')

]
