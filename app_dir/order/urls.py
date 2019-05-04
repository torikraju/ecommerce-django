from django.urls import path

from app_dir.order import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='list'),
    path('<order_id>/', views.OrderDetailView.as_view(), name='detail'),
]
