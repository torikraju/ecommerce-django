from django.urls import path

from app_dir.cart import views

urlpatterns = [
    path('', views.cart_home, name='home'),
    path('update/', views.cart_update, name='update'),
    path('checkout/', views.checkout_home, name='checkout'),
    path('checkout/success/', views.checkout_done_view, name='success'),
]
