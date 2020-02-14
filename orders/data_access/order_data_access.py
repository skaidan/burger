import datetime
import math

from inventory.data_access.inventory_data_access import InventoryDataAccess
from inventory.models import Types, DrinkTypes
from orders.interfaces.data_access.order_data_access_interface import OrderDataAccessInterface
from orders.models import Order, OrderElement, OrderStatus

EUROMANIA_PRICE = 1
DEADLINE_JARRAMANIA = datetime.datetime(2020, 9, 30, 0, 0, 0, 0)


class OrderDataAccess(OrderDataAccessInterface):
    order = None
    order_items = None
    creator = None

    def __init__(self, *args, **kwargs):
        super(OrderDataAccess, self).__init__(*args, **kwargs)

    def get_order(self, order_id):
        try:
            self.order = Order.objects.get(id=order_id)
        except Exception as exception:
            pass
        self.order_items = list(OrderElement.objects.filter(order_id=order_id))

    def get_by_author(self, author_id):
        return self._get_orders_by_author(author_id)

    def add_element_to_order(self, element):
        if self.order_items:
            self.order_items.append(element)
        else:
            self.order_items = [element, ]
        self._auto_check_complete_order_status()

    def save_new_order(self, order_entity, user):
        self.order = Order()
        self.order.created_by = user
        self.order.created_at = datetime.datetime.now()
        self.order.save()
        self._update_order_elements(user.id, order_entity)
        self._apply_offers()
        return self._order_total_price(self.order)

    def _update_order_elements(self, user_id, order_entity):
        for element in order_entity.elements:
            new_element = OrderElement()
            inventory_data_access = InventoryDataAccess()
            inventory = inventory_data_access.get_inventory_item_by_name(user_id, element.product)
            new_element.order = self.order
            new_element.price = inventory.price
            new_element.final_price = inventory.price
            new_element.inventory = inventory
            new_element.offer_number_in_order = 0
            new_element.save()

    def _apply_offers(self):
        self._euromania()
        while (self._menu_offer() is True or self._jarramania() is True):
            pass

    def load_order(self, order):
        self.get_order(order.id)
        return self._order_total_price(order)

    def _order_total_price(self, order):
        elements_prices = OrderElement.objects.filter(order=order)
        total_price = 0
        for element in elements_prices:
            total_price += element.final_price
        return self._two_decimals_rounded(total_price)

    def _menu_offer(self):
        found_burguer = False
        burguer_element = None
        found_fried = False
        fried_element = None
        found_drink = False
        drink_element = None
        next_offer = self._get_number_of_offers() + 1
        elements = OrderElement.objects.filter(order=self.order)
        for element in elements:
            if not element.offer:
                if element.inventory.type is Types.burguer and found_burguer is False:
                    burguer_element = element
                    found_burguer = True
                elif element.inventory.type is Types.potatoes and found_fried is False:
                    fried_element = element
                elif element.inventory.type in Types.drink and found_drink is False:
                    drink_element = element
            if burguer_element is not None and drink_element is not None and fried_element is not None:
                self._generate_offer_burguer(burguer_element, fried_element, drink_element, next_offer)
                return True
        return False

    def _generate_offer_burguer(self, burguer_element, fried_element, drink_element, next_offer):
        burguer_element.final_price = burguer_element.price * 0.85
        burguer_element.offer_number_in_order = next_offer
        burguer_element.offer = True
        burguer_element.save()
        fried_element.offer_number_in_order = next_offer
        fried_element.offer = True
        fried_element.save()
        drink_element.offer_number_in_order = next_offer
        drink_element.offer = True
        drink_element.save()

    def _euromania(self):
        if self.order.created_at.strftime("%A") is 'Sunday' or self.order.created_at.strftime("%A") is 'Wednesday':
            elements = OrderElement.objects.filter(order=self.order)
            for element in elements:
                if element.inventory.type is Types.potatoes:
                    element.final_price = EUROMANIA_PRICE

    def _jarramania(self):
        if self._jarramania_valid_period(datetime.datetime.today()):
            found_fried = False
            fried_element = None
            found_first_drink = False
            first_drink_element = None
            found_second_drink = False
            second_drink_element = None
            next_offer = self._get_number_of_offers() + 1
            elements = OrderElement.objects.filter(order=self.order)
            for element in elements:
                if not element.offer:
                    if element.inventory.type is Types.potatoes and found_fried is False:
                        fried_element = element
                        found_fried = True
                    elif element.inventory.subtype in DrinkTypes.Burribeer and found_first_drink is False:
                        first_drink_element = element
                        found_first_drink = True
                    elif element.inventory.type in DrinkTypes.Burribeer and found_first_drink is False:
                        second_drink_element = element
                        found_second_drink = True
            if fried_element and first_drink_element and second_drink_element:
                self._generate_jarramania(fried_element, first_drink_element, second_drink_element, next_offer)
            return False

    def _jarramania_valid_period(self, today):
        if today < DEADLINE_JARRAMANIA and self.order.created_at.hour > 15 and (
                self.order.created_at.hour < 19 or (
                self.order.created_at.hour is 19 and self.order.created_at.minute < 30)):
            return True
        else:
            return False

    def _generate_jarramania(self, fried_element, first_drink_element, second_drink_element, next_offer):
        fried_element.final_price = 1
        fried_element.offer_number_in_order = next_offer
        fried_element.offer = True
        fried_element.save()
        first_drink_element.final_price = 1
        first_drink_element.offer_number_in_order = next_offer
        first_drink_element.offer = True
        first_drink_element.save()
        second_drink_element.final_price = 1
        second_drink_element.offer_number_in_order = next_offer
        second_drink_element.offer = True
        second_drink_element.save()

    def _get_number_of_offers(self):
        offers = 0
        elements = OrderElement.objects.filter(order=self.order)
        for element in elements:
            if element.offer_number_in_order > offers:
                offers = element.offer_number_in_order
        return offers

    def _two_decimals_rounded(self, total_price):
        return math.floor(total_price * 100) / 100.0

    def _auto_check_complete_order_status(self):
        if self.order_items:
            for item in self.order_items:
                if item.served is False:
                    self.order.status = OrderStatus[2][1]
                    return False
        if self.order:
            self.order.status = OrderStatus[3][1]

    def _get_orders_by_author(self, author_id):
        class OrderEntity(self):
            paid = None
            status = None
            elements = []

            def __init__(self, order, order_elements):
                self.paid = order.paid
                self.status = order.status
                self.elements = list(order_elements)

        orders_by_author = []
        orders = Order.objects.filter(created_by=author_id)
        for order in orders:
            elements = OrderElement.objects.filter(order=order)
            order_by_author = OrderEntity(order, elements)
            orders_by_author.append(order_by_author)
        return orders_by_author
