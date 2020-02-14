import datetime
from django.test import testcases
from common.presenter.json_request_presenter import JSONRequestPresenter

DATETIME = datetime.datetime.now()


class SampleComplexClass(object):
    def __init__(self):
        self.list = [[1, 'a', DATETIME], {'z': {'a': 1, 'b': {'c': 111, 'd': {1: 2}}, 'e': [1, 2, 3]}, 'f': 'last'}, 23]
        self.field = 123


class JsonRequestPresenterTestCase(testcases.TestCase):
    def test_when_none_object_pass_to_convert_to_dict_then_empty_dict_is_returned(self):
        self.presenter = JSONRequestPresenter()
        result = self.presenter.get_successful_response_from_element_retrieval(None)
        self.assertEqual(result.data, None, "Obtained dictionary should be None")

    def test_when_complex_object_is_passed_to_be_converted_to_a_dict_then_dict_is_returned(self):
        self.presenter = JSONRequestPresenter()
        result = self.presenter.get_successful_response_from_element_retrieval(SampleComplexClass())
        self.assertEqual(result.data, self.expected_dictionary(), "Obtained value should be a dictionary")

    def expected_dictionary(self):
        return {'field': 123,
                'list': [[1, 'a', DATETIME],
                         {'z': {'a': 1, 'b': {'c': 111, 'd': {1: 2}}, 'e': [1, 2, 3]}, 'f': 'last'},
                         23]}
