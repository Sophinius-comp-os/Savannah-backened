"""
Default urls Configuration for savannah/orders
"""

from django.urls import path
from .views import (
    api_root,
    home,
    CustomerListCreateView,
    CustomerRetrieveUpdateDestroyView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', home, name='dashboard'),

    # API Root URL
    path('api-root/', api_root, name='api-root'),

    # Customer URLs
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-retrieve-update-destroy'),

    # Order URLs
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
]
