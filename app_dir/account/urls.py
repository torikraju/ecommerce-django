from django.urls import path

from app_dir.account import views

urlpatterns = [
    path('', views.AccountHomeView.as_view(), name='home'),
]
