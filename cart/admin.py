from django.contrib import admin
from .models import Cart,Cartitem

# Register your models here.

class Cartadmin(admin.ModelAdmin):
    list_display =['cart_id','date_added']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product','cart','quantity','is_active']




admin.site.register(Cart,Cartadmin)
admin.site.register(Cartitem,CartItemAdmin)
