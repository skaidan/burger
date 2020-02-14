from django.test import testcases
from mock import patch

from inventory.views import InventoryView
from orders.use_cases.get_inventory import GetInventoryUseCase

AUTH_USER_ID = 1
OK = 200


class InventoryViewsTestCase(testcases.TestCase):
    @patch.object(GetInventoryUseCase, 'run')
    def test_when_new_order_url_is_requested_then_get_inventory_use_case_is_called(self, mock_run):
        mock_run.return_value = ['Mocked', 'List']
        inventoryview = InventoryView()
        request = MockRequest
        user = {}
        user['user_id'] = AUTH_USER_ID
        request.GET = user
        inventoryview.get(request, AUTH_USER_ID)
        mock_run.assert_called_once()


class MockRequest():
    GET = None
