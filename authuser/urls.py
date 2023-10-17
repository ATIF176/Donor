from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userlogin, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]