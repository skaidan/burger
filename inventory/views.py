from rest_framework.views import APIView

from common.presenter.json_request_presenter import JSONRequestPresenter
from orders.use_cases.get_inventory import GetInventoryUseCase


class InventoryView(APIView):
    presenter = JSONRequestPresenter()

    def __init__(self, *args, **kwargs):
        APIView.__init__(self, *args, **kwargs)

    def get(self, request, user_id=None):
        try:
            inventory_available = GetInventoryUseCase()
            inventory_available.run(user_id)
            return self.presenter.get_successful_response_from_element_retrieval(inventory_available.get())
        except Exception as exception:
            return self.presenter.get_error_response_internal_error(exception.message)

    def post(self, request):
        pass

    def patch(self, request):
        pass
