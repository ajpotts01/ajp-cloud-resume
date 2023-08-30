# Django imports
from django.db import models
from django.utils import timezone


# Create your models here.
# CI trigger
class Visit(models.Model):
    page: models.CharField = models.CharField(max_length=25)
    visit_time: models.DateTimeField = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Visited {self.page} on {self.visit_time}"

class Job(models.Model):
    title: models.CharField = models.CharField(max_length=250)
    company: models.CharField = models.CharField(max_length=250)
    start_date: models.DateField = models.DateField()
    end_date: models.DateField = models.DateField()
    description: models.CharField = models.CharField(max_length=250)

class Certification(models.Model):
    title: models.CharField = models.CharField(max_length=250)
    issued_by: models.CharField = models.CharField(max_length=250)
    issued_date: models.DateField = models.DateField()

class Education(models.Model):
    title: models.CharField = models.CharField(max_length=250)
    school: models.CharField = models.CharField(max_length=250)
    start_year: models.IntegerField = models.IntegerField()
    end_year: models.IntegerField = models.IntegerField()