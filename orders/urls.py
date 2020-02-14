from django.conf.urls import url, include
from rest_framework import routers

from inventory.views import InventoryView
from orders.views import OrdersView

router = routers.DefaultRouter()

# router.register(r'myproject', views.TransactionsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^order/$', OrdersView.as_view(), name='order'),
    url(r'^staffmember/(?P<user_id>\d+)/orders/$', OrdersView.as_view(), name='orders'),
    url(r'^inventory/(?P<user_id>\d+)/$', InventoryView.as_view(), name='inventory'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
