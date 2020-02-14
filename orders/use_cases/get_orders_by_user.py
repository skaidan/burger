from common.interface.use_case_base_interface import UseCaseBaseInterface
from orders.data_access.order_data_access import OrderDataAccess


class GetOrdersByUserUseCase(UseCaseBaseInterface):
    orders = []

    def run(self, user_id, input_entity=None):
        order_data_access = OrderDataAccess()
        self.orders = order_data_access.get_by_author(user_id)

    def get(self):
        return self.orders
