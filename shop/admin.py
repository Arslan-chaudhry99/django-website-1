from django.contrib import admin
from .models import Category,Product
# Register your models here.

# Category
@admin.register(Category)  #decorator
class CategoryAdmin(admin.ModelAdmin):
    list_display=('slug','name','imge', 'status', 'created_at' )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('slug','name','product_imge','created_at' )

