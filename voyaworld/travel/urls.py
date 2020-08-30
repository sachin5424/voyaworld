from django.contrib import admin
from django.urls import path,include
from travel import views
from  django.views.generic import RedirectView
app_name='travel'
urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('packages/', views.packages,name='packages'),
    path('contact/', views.contact,name='contact'),
    path('about-us/', views.about,name='about'),
    path('packages/<str:slug>/', views.packagesDetail,name='packagesDetail'),
    path('', RedirectView.as_view(url="home/")),
    
]