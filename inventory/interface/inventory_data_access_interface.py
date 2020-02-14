from abc import abstractmethod


class InventoryDataAccessInterface(object):

    @abstractmethod
    def get_inventory(self, user_id):
        pass

    @abstractmethod
    def get_inventory_item(self, user_id, id):
        pass

    @abstractmethod
    def reserve_inventory_item(self, user_id, id):
        pass

    @abstractmethod
    def release_inventory_item(self, user_id, id):
        pass
