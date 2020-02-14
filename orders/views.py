import json

from rest_framework.views import APIView

from common.presenter.json_request_presenter import JSONRequestPresenter
from orders.use_cases.generate_order import GenerateOrderUseCase
from orders.use_cases.get_order_price import GetOrderPriceUseCase
from orders.use_cases.get_orders_by_user import GetOrdersByUserUseCase

SESSION_USER_ID = 1


class OrdersView(APIView):
    presenter = JSONRequestPresenter()

    def __init__(self, *args, **kwargs):
        APIView.__init__(self, *args, **kwargs)

    def get(self, request, user_id=None):
        try:
            list_of_orders = GetOrdersByUserUseCase()
            list_of_orders.run(user_id)
            return self.presenter.get_successful_response_from_element_retrieval(list_of_orders.get())
        except Exception as exception:
            return self.presenter.get_error_response_internal_error(exception.message)

    def post(self, request, user_id=None):
        try:
            order = OrderEntity(json.loads(request.data['order']))
            if 'save' in request.data:
                if order.elements:
                    generate_order_use_case = GenerateOrderUseCase()
                    generate_order_use_case.run(user_id, order)
                    return self.presenter.get_successful_response_from_element_retrieval(generate_order_use_case.get())

            else:
                if order.id:
                    get_order_price_use_case = GetOrderPriceUseCase()
                    get_order_price_use_case.run(order)
                    return self.presenter.get_successful_response_from_element_retrieval(get_order_price_use_case.get())

        except Exception as exception:
            return self.presenter.get_error_response_internal_error(exception.message)

        return self.presenter.get_successful_response_with_empty_response()

    def patch(self, request):
        pass


class OrderEntity(object):
    id = None
    elements = None

    def __init__(self, order):
        if 'id' in order:
            self.id = order['id']
        if 'elements' in order:
            element = OrderElementEntity()
            for item in order['elements']:
                if 'id' in item and 'amount' in item:
                    element.inventory_id = item['id']
                    element.amount = item['amount']
                    element.product = item['product']
                if self.elements is None:
                    self.elements = [element, ]
                else:
                    self.elements.append(element)


class OrderElementEntity(object):
    inventory_id = None
    amount = None
    product = None
