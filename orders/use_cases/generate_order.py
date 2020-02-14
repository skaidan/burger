from common.interface.use_case_base_interface import UseCaseBaseInterface
from orders.data_access.order_data_access import OrderDataAccess


class GenerateOrderUseCase(UseCaseBaseInterface):
    total_price = 0
    def run(self, user_id, input_entity=None):
        order_data_access = OrderDataAccess()
        if input_entity:
            self.total_price = order_data_access.save_new_order(input_entity, user_id)

    def get(self):
        return self.total_price
