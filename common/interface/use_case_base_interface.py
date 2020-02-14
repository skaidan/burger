from abc import abstractmethod


class UseCaseBaseInterface(object):

    @abstractmethod
    def run(self, user_id, input_entities=None):
        pass

    @abstractmethod
    def get(self):
        pass
