from django.contrib.gis.db import models


class InventoryManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)


