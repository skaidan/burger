from inventory.interface.inventory_data_access_interface import InventoryDataAccessInterface
from inventory.models import Inventory
from organizations.models import StaffMember


class InventoryDataAccess(InventoryDataAccessInterface):

    def get_inventory(self,user_id):
        staffmember = StaffMember.objects.get(id=user_id)
        inventory = Inventory.objects.filter(restaurant = staffmember.restaurant)
        inventory_entities = []
        for item in inventory:
            inventory_entities.append(InventoryEntity(item))
        return inventory_entities


    def get_inventory_item_by_name(self,user_id, product):
        staffmember = StaffMember.objects.get(id=user_id)
        return Inventory.objects.get(restaurant = staffmember.restaurant, product = product)

    def get_inventory_item_by_id(self,user_id, id):
        staffmember = StaffMember.objects.get(id=user_id)
        return Inventory.objects.get(restaurant = staffmember.restaurant, id = id)

    def reserve_inventory_item_by_id(self,user_id, id):
        staffmember = StaffMember.objects.get(id=user_id)
        item = Inventory.objects.get(restaurant=staffmember.restaurant, id = id)
        if item.remaining_items > 0:
            item.reserved = item.reserved  + 1
            item.save()

    def reserve_inventory_item_by_name(self, user_id, product):
        staffmember = StaffMember.objects.get(id=user_id)
        item = Inventory.objects.get(restaurant=staffmember.restaurant, product=product)
        if item.remaining_items > 0:
            item.reserved = item.reserved + 1
            item.save()


    def release_inventory_item_by_id(self,user_id, id):
        staffmember = StaffMember.objects.get(id=user_id)
        item = Inventory.objects.get(restaurant=staffmember.restaurant, id = id)
        if item.remaining_items > 0:
            item.reserved = item.reserved - 1
            item.save()

    def release_inventory_item_by_name(self, user_id, product):
        staffmember = StaffMember.objects.get(id=user_id)
        item = Inventory.objects.get(restaurant=staffmember.restaurant, product=product)
        if item.remaining_items > 0:
            item.reserved = item.reserved - 1
            item.save()


class InventoryEntity(object):
    product_id = None
    product = None
    type = None
    subtype = None
    price = None
    in_store = None
    reserved = None
    remaining = None

    def __init__(self, inventory):
        self.product_id = inventory.id
        self.product = inventory.product
        self.type = inventory.type
        self.subtype = inventory.subtype
        self.price = inventory.price
        self.in_store = inventory.in_store
        self.reserved = inventory.reserved
        self.remaining = inventory.remaining_items
