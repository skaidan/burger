from __future__ import unicode_literals
from django.contrib.gis.db import models
from organizations.managers import RestaurantManager, StaffMemberManager


class Restaurant(models.Model):
    objects = RestaurantManager()


class StaffMember(models.Model):

    objects = StaffMemberManager()
    restaurant = models.ForeignKey(Restaurant)
    name = models.TextField(null=False,default='default')