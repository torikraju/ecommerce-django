from django.urls import path

from app_dir.search import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='list')
]
