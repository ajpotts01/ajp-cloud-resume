# Django imports
from django.db import models
from django.utils import timezone


# Create your models here.
# CI trigger
class Visit(models.Model):
    page: models.CharField = models.CharField(max_length=25)
    visit_time: models.DateTimeField = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"Visited {self.page} on {self.visit_time}"


class Job(models.Model):
    title: models.CharField = models.CharField(max_length=250)
    company: models.CharField = models.CharField(max_length=250)
    start_date: models.CharField = models.CharField(max_length=100)
    end_date: models.CharField = models.CharField(max_length=100)
    description: models.CharField = models.CharField(max_length=250)
    job_number: models.IntegerField = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} - {self.company}"


class Certification(models.Model):
    title: models.CharField = models.CharField(max_length=250)
    issued_by: models.CharField = models.CharField(max_length=250)
    issued_date: models.DateField = models.DateField()
    url: models.URLField = models.URLField(blank=True)
    image: models.ImageField = models.ImageField(upload_to="certs/images/")

    def __str__(self) -> str:
        return f"{self.issued_by} - {self.title}"


class Education(models.Model):
    title: models.CharField = models.CharField(max_length=250)
    school: models.CharField = models.CharField(max_length=250)
    start_year: models.IntegerField = models.IntegerField()
    end_year: models.IntegerField = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.school} - {self.title}"


class Skill(models.Model):
    type: models.CharField = models.CharField(max_length=100)  # TODO: Change to enum?
    proficiency: models.CharField = models.CharField(
        max_length=100
    )  # TODO: Change to enum?

    def __str__(self) -> str:
        return self.type
