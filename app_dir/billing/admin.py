from django.contrib import admin

from app_dir.billing.models import BillingProfile, Card

admin.site.register(BillingProfile)
admin.site.register(Card)
