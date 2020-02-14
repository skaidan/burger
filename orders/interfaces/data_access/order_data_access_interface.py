from abc import abstractmethod


class OrderDataAccessInterface(object):
    pass

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_order(self, order_id):
        pass

    @abstractmethod
    def get_by_author(self, author_id):
        pass

    @abstractmethod
    def add_element_to_order(self, element):
        pass

    @abstractmethod
    def load_order(self, order):
        pass

    @abstractmethod
    def save_new_order(self, order_entity, user_id):
        pass
