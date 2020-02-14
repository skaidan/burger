from __future__ import unicode_literals

from django.contrib.gis.db import models
from enum import Enum

from inventory.managers import InventoryManager
from organizations.models import Restaurant

class Types(Enum):
    burguer = 1
    drink = 2
    potatoes = 3

class DrinkTypes(Enum):
    Burricola = 1
    Burribeer = 2
    Brawndo = 3

class Inventory(models.Model):
    objects = InventoryManager()
    product = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    subtype = models.CharField(max_length=60)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10, max_length=12)
    in_store = models.IntegerField(default=0, null=False)
    reserved = models.IntegerField(default=0, null=False)
    restaurant = models.ForeignKey(Restaurant)

    @property
    def remaining_items(self):
        return self.in_store - self.reserved