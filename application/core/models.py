# Standard lib imports
import datetime as dt

# Django imports
from django.db import models


# Create your models here.
class Visit(models.Model):
    page: models.CharField = models.CharField(max_length=25)
    visit_time: models.DateTimeField = models.DateTimeField(default=dt.datetime.utcnow)

    def __str__(self):
        return f"Visited {self.page} on {self.visit_time}"