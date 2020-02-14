from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED, \
    HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_405_METHOD_NOT_ALLOWED, HTTP_500_INTERNAL_SERVER_ERROR

from rest_framework.response import Response

from common.interface.request_presenter_interface import RequestPresenterInterface


class JSONRequestPresenter(RequestPresenterInterface):
    HTTP_422_UNPROCESSABLE_ENTITY = 422

    def __init__(self):
        super(JSONRequestPresenter, self).__init__()

    def get_successful_response_from_list_retrieval(self, list_of_elements):
        element_as_dictionary = self.convert_object_to_dictionary(list_of_elements)
        return Response(data=element_as_dictionary, status=HTTP_200_OK)

    def get_successful_response_from_element_retrieval(self, retrieved_element):
        element_as_dictionary = self.convert_object_to_dictionary(retrieved_element)
        return Response(data=element_as_dictionary, status=HTTP_200_OK)

    def get_successful_response_from_element_creation(self, created_element):
        element_as_dictionary = self.convert_object_to_dictionary(created_element)
        return Response(data=element_as_dictionary, status=HTTP_201_CREATED)

    def get_successful_response_with_custom_message(self, custom_message):
        message = self.build_error_message(custom_message)
        return Response(data=message, status=HTTP_201_CREATED)

    def get_successful_response_from_element_update(self, updated_element):
        element_as_dictionary = self.convert_object_to_dictionary(updated_element)
        return Response(data=element_as_dictionary, status=HTTP_200_OK)

    def get_successful_response_from_element_deletion(self):
        return Response(status=HTTP_204_NO_CONTENT)

    def get_successful_response_with_empty_response(self):
        return Response(status=HTTP_204_NO_CONTENT)

    def get_error_response_not_enough_permissions_to_perform_action(self):
        message = self.build_error_message("unauthorized")
        return Response(data=message, status=HTTP_401_UNAUTHORIZED)

    def get_error_response_forbidden_action(self):
        message = self.build_error_message("forbidden")
        return Response(data=message, status=HTTP_403_FORBIDDEN)

    def get_error_response_resource_not_found(self, name_of_type_of_resource=None):
        message = self.build_error_message("{entity} not found".format(entity=name_of_type_of_resource))
        return Response(data=message, status=HTTP_404_NOT_FOUND)

    def get_error_response_method_not_allowed(self):
        message = self.build_error_message("method not allowed")
        return Response(data=message, status=HTTP_405_METHOD_NOT_ALLOWED)

    def get_error_response_wrong_fields_in_resource(self, field_level_errors=None):
        message = self.build_error_message("unprocessable entity", field_level_errors)
        return Response(data=message, status=self.HTTP_422_UNPROCESSABLE_ENTITY)

    def get_error_response_internal_error(self, exception_message):
        message = self.build_error_message('internal_error', {'exception': exception_message})
        return Response(data=message, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def convert_object_to_dictionary(self, element):
        if isinstance(element, dict):
            data = {}
            for (k, v) in element.items():
                data[k] = self.convert_object_to_dictionary(v)
            return data
        elif hasattr(element, "__dict__"):
            data = dict([(key, self.convert_object_to_dictionary(value))
                         for key, value in element.__dict__.iteritems()
                         if not callable(value) and not key.startswith('_')])
            return data
        elif hasattr(element, "__iter__"):
            return [self.convert_object_to_dictionary(v) for v in element]
        else:
            return element

    def build_error_message(self, message, errors=None):
        return_data = {"message": message}
        if errors is not None:
            return_data["errors"] = self.convert_object_to_dictionary(errors)
        return return_data
