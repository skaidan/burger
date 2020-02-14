from __future__ import unicode_literals

import datetime

from django.contrib.gis.db import models

from inventory.models import Inventory
from orders.managers import OrderElementManager, OrderManager
from organizations.models import StaffMember

OrderStatus = (
    ('OPEN', 'Open'),
    ('ORDERED', 'Ordered'),
    ('IN_PROGRESS', 'In progress'),
    ('COMPLETE', 'Complete'),
    ('RELEASED', 'Released'))


class Order(models.Model):
    objects = OrderManager()
    paid = models.BooleanField(default=False, blank=False, null=False)
    status = models.CharField(max_length=20, choices=OrderStatus, default='Open')
    created_by = models.ForeignKey(StaffMember, null=False, blank=False, default=1)
    created_at = models.DateTimeField(default=datetime.datetime.now)


class OrderElement(models.Model):
    objects = OrderElementManager()
    order = models.ForeignKey(Order, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    final_price = models.DecimalField(decimal_places=2, max_digits=10)
    offer = models.BooleanField(default=False, null=False)
    offer_number_in_order = models.IntegerField()
    in_offer = models.BooleanField(default=False, null=False)
    served = models.BooleanField(default=False, null=False)
    inventory = models.ForeignKey(Inventory, null=False, blank=False)
    product = models.CharField(max_length=60)
