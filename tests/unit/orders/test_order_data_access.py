import datetime

from django.test import testcases
from mock import patch
import orders
from inventory.models import Inventory
from orders.data_access.order_data_access import OrderDataAccess
from orders.models import Order, OrderElement
from organizations.models import Restaurant, StaffMember

AUTHOR_ID = 1


class TestOrderDataAccessTestCase(testcases.TestCase):
    def test_when_last_element_is_not_served_then_status_is_on_progress(self):
        order_data_access = OrderDataAccess()
        order_data_access.order = self._initialize_order()
        first_element = MockOrderElement(2, True)
        second_element = MockOrderElement(5, False)
        order_data_access.add_element_to_order(first_element)
        expected_value = 'Complete'
        self.assertEqual(order_data_access.order.status, expected_value,
                         'Error, status should be {value}.'.format(value=expected_value))
        order_data_access.add_element_to_order(second_element)
        expected_value = 'In progress'
        self.assertEqual(order_data_access.order.status, expected_value,
                         'Error, status should be {value}.'.format(value=expected_value))

    def test_when_not_all_element_are_served_then_status_is_on_progress(self):
        order_data_access = OrderDataAccess()
        order_data_access.order = self._initialize_order()
        first_element = MockOrderElement(5, False)
        second_element = MockOrderElement(2, True)
        order_data_access.add_element_to_order(first_element)
        order_data_access.add_element_to_order(second_element)
        expected_value = 'In progress'
        self.assertEqual(order_data_access.order.status, expected_value,
                         'Error, status should be {value}.'.format(value=expected_value))

    def test_when_a_order_is_created_and_has_elements_then_total_price_is_returned(self):
        order_data_access = OrderDataAccess()
        order, staffmember = self._initialize_method_from_storage()
        total_price = order_data_access._order_total_price(order)
        expected_value = 7.42
        self.assertTrue(total_price == expected_value,
                         'Error, total price is {total_price}, and should be {value}.'.format(total_price=total_price,value=expected_value))

    @patch.object(orders.data_access.order_data_access.OrderDataAccess, '_get_orders_by_author')
    def test_when_user_has_orders_then_orders_are_returned(self, mock_get_orders_by_author):
        mock_get_orders_by_author.return_value = [MockObjectEntity(), ]
        order_data_access = OrderDataAccess()
        orders = order_data_access.get_by_author(AUTHOR_ID)
        self.assertEqual(orders[0].status, 'Mocked', 'Error, status should be "Mocked".')

    def test_when_an_order_is_created_on_Monday_then_euromania_offer_does_not_applies(self):
        order_data_access = OrderDataAccess()
        order, staffmember = self._initialize_method_from_storage()
        total_price = order_data_access._order_total_price(order)
        order_data_access.order = order
        order_data_access._euromania()
        total_price_offer_applied = order_data_access._order_total_price(order)
        self.assertEqual(total_price,total_price_offer_applied, "Error, price should not be modified.")

    def _initialize_order(self, paid=False, status='In progress'):
        return MockOrder(paid, status)

    def _initialize_method_from_storage(self):
        order = Order()
        order.created_at = datetime.datetime(2020, 1, 27, 0, 0, 0, 1)
        order.save()
        restaurant = Restaurant()
        restaurant.save()
        staffmember = StaffMember()
        staffmember.restaurant = restaurant
        staffmember.save()
        inventory = Inventory()
        inventory.in_store = 10
        inventory.product = 'mocked_product'
        inventory.restaurant = restaurant
        inventory.save()
        element = OrderElement()
        element.price = 5.31
        element.inventory = inventory
        element.product = 'mocked_product'
        element.order = order
        element.final_price = 5.31
        element.offer_number_in_order = 0
        element.save()
        order.elements = [element,]
        element = OrderElement()
        element.price = 2.11
        element.final_price = 2.11
        element.offer_number_in_order = 0
        element.order = order
        element.product = 'mocked_product'
        element.inventory = inventory
        element.save()
        order.elements.append(element)
        order.save()
        return order, staffmember

class MockObjectEntity(object):
    paid = False
    status = 'Mocked'
    elements = ['Mocked element', ]


class MockOrder(object):
    paid = None
    status = None
    created_by = AUTHOR_ID
    elements = []

    def __init__(self, paid, status):
        self.paid = paid
        self.status = status


class MockOrderElement(object):
    final_price = None
    served = None

    def __init__(self, final_price, served):
        self.final_price = final_price
        self.served = served
