from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_jwt.views import obtain_jwt_token

from app_dir.account.views import guest_register_view, RegisterView, LoginView
from app_dir.address.views import checkout_address_create_view, checkout_address_reuse_view
from app_dir.billing.views import payment_method_view, payment_method_createview
from app_dir.cart.views import cart_detail_api_view
from app_dir.marketing.views import MarketingPreferenceUpdateView, MailchimpWebhookView
from .views import home_page, about, contact

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about),
    path('contact', contact, name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('billing/payment-method/', payment_method_view, name='billing-payment-method'),
    path('billing/payment-method/create/', payment_method_createview, name='billing-payment-method-endpoint'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('api-token-auth', obtain_jwt_token),
    path('user/', include(('app_dir.user.urls', 'user'), namespace='user')),
    path('api/user/', include(('app_dir.user.api.urls', 'user_api'), namespace='user_api')),
    path('api/module/', include(('app_dir.module.api.urls', 'module_api'), namespace='module_api')),
    path('product/', include(('app_dir.products.urls', 'product'), namespace='product')),
    path('search/', include(('app_dir.search.urls', 'search'), namespace='search')),
    path('settings/email/', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    path('cart/', include(('app_dir.cart.urls', 'cart'), namespace='cart')),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include(('app_dir.account.urls', 'account'), namespace='account')),
    path('webhooks/mailchimp/', MailchimpWebhookView.as_view(), name='webhooks-mailchimp'),
    path('settings/', RedirectView.as_view(url='/account')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
