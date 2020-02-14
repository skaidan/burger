import json

from django.test import testcases
from mock import patch
from rest_framework.reverse import reverse

from orders.use_cases.generate_order import GenerateOrderUseCase
from orders.use_cases.get_order_price import GetOrderPriceUseCase
from orders.use_cases.get_orders_by_user import GetOrdersByUserUseCase
from orders.views import OrdersView

AUTH_USER_ID = 1
OK = 200


class OrderViewsTestCase(testcases.TestCase):

    @patch.object(GetOrdersByUserUseCase, 'get')
    def test_when_get_list_orders_by_user_url_is_requested_then_get_orders_by_user_use_case_is_called(self, mock_get):
        mock_get.return_value = OK
        url = reverse('orders', kwargs={'user_id': AUTH_USER_ID})
        response = self.client.get(url, data={'user_id': AUTH_USER_ID})
        self.assertEqual(response.status_code, mock_get.return_value,
                         'Error, returned value was {returned} and should be {value}'.format(
                             returned=response.status_code, value=mock_get.return_value))

    @patch.object(GetOrderPriceUseCase, 'run')
    def test_when_get_order_price_url_is_requested_then_get_order_price_use_case_is_called(self, mock_run):
        mock_run.return_value = ['Mocked', 'List']
        ordersview = OrdersView()
        request = MockRequest()
        order = {}
        element = {}
        order['id'] = 1
        element['id'] = 1
        element['amount'] = 2
        element['product'] = 'mocked_product'
        order['elements'] = [element, ]
        request.data = {}
        request.data['order'] = json.dumps(order)
        request.POST = order
        ordersview.post(request, AUTH_USER_ID)
        mock_run.assert_called_once()

    @patch.object(GenerateOrderUseCase, 'run')
    def test_when_generate_order_url_is_requested_then_generate_order_use_case_is_called(self, mock_run):
        mock_run.return_value = ['Mocked', 'List']
        ordersview = OrdersView()
        request = MockRequest()
        order = {}
        element = {}
        order['id'] = 1
        element['id'] = 1
        element['amount'] = 2
        element['product'] = 'mocked_product'
        order['elements'] = [element, ]
        request.data = {}
        request.data['order'] = json.dumps(order)
        request.data['save'] = 'mocked_value'
        request.POST = order
        ordersview.post(request, AUTH_USER_ID)
        mock_run.assert_called_once()

    @patch.object(GetOrdersByUserUseCase, 'get')
    def test_when_we_request_orders_by_user_id_then_list_of_orders_returned(self, mock_get):
        mock_get.return_value = ['Mocked', 'List']
        view = OrdersView()
        request = MockRequest()
        user = {}
        user['user_id'] = AUTH_USER_ID
        request.GET = user
        returned_value = view.get(request, AUTH_USER_ID)
        self.assertEqual(returned_value.data, mock_get.return_value,
                         'Error, returned value was {returned} and should be {value}'.format(
                             returned=returned_value.data, value=mock_get.return_value))


class MockRequest():
    GET = None
