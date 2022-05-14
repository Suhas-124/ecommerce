from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
path('', views.store_view,name='store'),
path('<slug:category_slug>/', views.store_view,name='products_by_category'),
path('<slug:category_slug>/<slug:product_slug>/', views.product_detail_view,name='product_detail'),



]
