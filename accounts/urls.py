from django.contrib import admin
from django.urls import path,include
from accounts import views



urlpatterns = [
path('register/', views.register, name='register'),
path('login/', views.login, name='login'),
path('logout/', views.logout, name='logout'),
path('dashboard/', views.dashboard, name='dashboard'),
path('', views.dashboard, name='dashboard'),
path('forgotpassword/', views.forgotpassword, name='forgotpassword'),




# path('activate/<uidb64>/<token>/', views.activate, name='activate'),




]
