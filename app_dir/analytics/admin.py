from django.contrib import admin

from app_dir.analytics.models import ObjectViewed, UserSession

admin.site.register(ObjectViewed)
admin.site.register(UserSession)
