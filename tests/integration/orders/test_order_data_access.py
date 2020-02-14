from django.test import testcases

from inventory.models import Inventory
from orders.data_access.order_data_access import OrderDataAccess
from orders.models import Order, OrderElement, OrderStatus
from organizations.models import Restaurant


class OrderDataAccessIntegrationTestCase(testcases.TestCase):
    order = None
    elements = None

    def setUp(self):
        self.order = self._initialize_order()

    def test_when_data_access_is_called_then_order_is_retrieved_from_origin_of_data(self):
        order_data_access = OrderDataAccess()
        order_data_access.get_order(self.order.id)
        self.assertTrue(order_data_access.order.paid,
                        'Error, paid status should be True. Check connection to SourceData')

    def test_when_data_access_is_called_then_order_elements_are_retrieved_from_origin_of_data(self):
        self.elements = self._initialize_elements()
        order_data_access = OrderDataAccess()
        order_data_access.get_order(self.order.id)
        expected_number_of_elements_in_order = 1
        self.assertEqual(expected_number_of_elements_in_order, len(order_data_access.order_items),
                         'Error, items number should be {expected}'.format(
                             expected=expected_number_of_elements_in_order))

    def _initialize_order(self):
        order = Order()
        order.paid = True
        order.status = OrderStatus[0][0]
        order.save()
        return order

    def _initialize_elements(self):
        restaurant = Restaurant()
        restaurant.save()
        inventory = Inventory()
        inventory.restaurant = restaurant
        inventory.save()
        element = OrderElement()
        element.order_id = self.order.id
        element.final_price = 5
        element.offer_number_in_order = 0
        element.price = 5
        element.inventory = inventory
        element.save()
        return [element, ]
