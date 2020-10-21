from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import url
from .views import contactView, successView

urlpatterns = [
    path('', views.home, name='home'),
    path('administration/', views.administration, name='administration'),
    path('Future/', views.Future, name='Future'),
    path('fees/', views.fees, name='fees'),
   # path('contact/', views.contact, name='contact'),
    path('facilities/', views.facilities, name='facilities'),
    path('Gallaries/', views.Gallaries, name='Gallaries'),
    path('holiday/', views.holiday, name='holiday'),
    path('honors/', views.honors, name='honors'),
    path('news/', views.news, name='news'),
    path('Rules/', views.Rules, name='Rules'),
    path('school/', views.school, name='school'),
    #path('email/', views.school, name='email'),

   # path('email/', contactView, name='email'),
    path('success/', successView, name='success'),
    path('contact/', contactView, name='contact'),
    
]