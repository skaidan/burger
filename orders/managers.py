from django.contrib.gis.db import models


class OrderElementManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)


class OrderManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)
