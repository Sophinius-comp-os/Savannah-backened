"""
savannah URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from orders.views import login_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
    path('accounts/', include('allauth.urls')),
    path('', login_redirect),
]
