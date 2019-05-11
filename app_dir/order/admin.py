from django.contrib import admin

from app_dir.order.models import Order, ProductPurchase

admin.site.register(Order)
admin.site.register(ProductPurchase)
