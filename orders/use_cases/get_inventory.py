from common.interface.use_case_base_interface import UseCaseBaseInterface
from inventory.data_access.inventory_data_access import InventoryDataAccess


class GetInventoryUseCase(UseCaseBaseInterface):
    inventory = []

    def run(self, user_id, input_entity=None):
        inventory_data_access = InventoryDataAccess()
        self.inventory = inventory_data_access.get_inventory(user_id)

    def get(self):
        return self.inventory
