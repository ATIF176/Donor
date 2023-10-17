from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name="register"),
    path('profile/<int:pk>', views.profile, name="profile"),
    path('donorlist/', views.donorlist, name="donorlist"),
]