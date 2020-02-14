from common.interface.use_case_base_interface import UseCaseBaseInterface
from orders.data_access.order_data_access import OrderDataAccess


class GetOrderPriceUseCase(UseCaseBaseInterface):
    user_id = None
    order = None
    total_price = None

    def run(self, user_id, input_entity=None):
        order_data_access = OrderDataAccess()
        if input_entity:
            self.total_price = order_data_access.load_order(input_entity)

    def get(self):
        return self.total_price
