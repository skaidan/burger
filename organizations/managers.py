from django.contrib.gis.db import models


class RestaurantManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)


class StaffMemberManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)