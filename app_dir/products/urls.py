from django.urls import path

from app_dir.products import views

urlpatterns = [
    path('list-view/', views.ProductListView.as_view(), name='list'),
    path('detail-view/<slug:slug>/', views.ProductDetailSlugView.as_view(), name='details'),
]
