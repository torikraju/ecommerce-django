from django.contrib import admin

from app_dir.products.models import Product


class ProductCustomAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_digital']


admin.site.register(Product, ProductCustomAdmin)

# Register your models here.
