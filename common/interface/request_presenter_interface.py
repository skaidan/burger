from abc import abstractmethod


class RequestPresenterInterface(object):
    def __init__(self):
        pass

    @abstractmethod
    def get_successful_response_from_list_retrieval(self, list_of_elements):
        pass

    @abstractmethod
    def get_successful_response_from_element_retrieval(self, retrieved_element):
        pass

    @abstractmethod
    def get_successful_response_from_element_creation(self, created_element):
        pass

    @abstractmethod
    def get_successful_response_with_custom_message(self, custom_message):
        pass

    @abstractmethod
    def get_successful_response_from_element_update(self, updated_element):
        pass

    @abstractmethod
    def get_successful_response_from_element_deletion(self):
        pass

    @abstractmethod
    def get_successful_response_with_empty_response(self):
        pass

    @abstractmethod
    def get_error_response_not_enough_permissions_to_perform_action(self):
        pass

    @abstractmethod
    def get_error_response_forbidden_action(self):
        pass

    @abstractmethod
    def get_error_response_resource_not_found(self, name_of_type_of_resource=None):
        pass

    @abstractmethod
    def get_error_response_method_not_allowed(self):
        pass

    @abstractmethod
    def get_error_response_wrong_fields_in_resource(self, field_level_errors=None):
        pass

    @abstractmethod
    def get_error_response_internal_error(self, exception_message):
        pass
