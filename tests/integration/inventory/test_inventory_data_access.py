from django.test import testcases

from inventory.data_access.inventory_data_access import InventoryDataAccess
from inventory.models import Inventory
from organizations.models import StaffMember, Restaurant

USER_ID = 1


class InventoryDataAccessIntegrationTestCase(testcases.TestCase):
    order = None
    elements = None

    def setUp(self):
        self.order = self._initialize_inventory(USER_ID)

    def test_when_data_access_is_called_then_inventory_is_retrieved_from_origin_of_data(self):
        inventory_data_access = InventoryDataAccess()
        expected_number_of_elements_in_inventory = 1
        self.assertEqual(expected_number_of_elements_in_inventory, len(inventory_data_access.get_inventory(USER_ID)),
                         'Error, items number should be {expected}'.format(
                             expected=expected_number_of_elements_in_inventory))

    def _initialize_inventory(self, user_id):
        restaurant = Restaurant()
        restaurant.save()
        staff_member = StaffMember()
        staff_member.restaurant = restaurant
        staff_member.save()
        inventory = Inventory()
        inventory.restaurant = restaurant
        inventory.product = 'default product'
        inventory.price = 5
        inventory.save()
        return inventory
