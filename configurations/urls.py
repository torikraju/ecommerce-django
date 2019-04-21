from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from app_dir.account.views import login_page, register_page, guest_register_view
from app_dir.address.views import checkout_address_create_view, checkout_address_reuse_view
from .views import home_page, about, contact

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about),
    path('contact', contact, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('api-token-auth', obtain_jwt_token),
    path('user/', include(('app_dir.user.urls', 'user'), namespace='user')),
    path('api/user/', include(('app_dir.user.api.urls', 'user_api'), namespace='user_api')),
    path('api/module/', include(('app_dir.module.api.urls', 'module_api'), namespace='module_api')),
    path('product/', include(('app_dir.products.urls', 'product'), namespace='product')),
    path('search/', include(('app_dir.search.urls', 'search'), namespace='search')),
    path('cart/', include(('app_dir.cart.urls', 'cart'), namespace='cart')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
