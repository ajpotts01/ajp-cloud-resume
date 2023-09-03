# Django imports
from django.http import HttpRequest, HttpResponse
from django.test import TestCase

# Project imports
from .models import Visit


# Create your tests here.
# TODO: Consider pytest?
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response: HttpResponse = self.client.get("/")

        self.assertTemplateUsed(response=response, template_name="core/about.html")
        self.assertTemplateUsed(response=response, template_name="core/base.html")

    def test_home_registers_visit(self):
        response: HttpResponse = self.client.get("/")

        self.assertEqual(first=Visit.objects.count(), second=1)


class ContactPageTest(TestCase):
    def test_uses_contact_template(self):
        response: HttpResponse = self.client.get("/contact")

        self.assertTemplateUsed(response=response, template_name="core/contact.html")

    def test_contact_registers_visit(self):
        response: HttpResponse = self.client.get("/contact")

        self.assertEqual(first=Visit.objects.count(), second=1)


class ResumePageTest(TestCase):
    def test_uses_resume_template(self):
        response: HttpResponse = self.client.get("/resume")

        self.assertTemplateUsed(response=response, template_name="core/resume.html")
        self.assertTemplateUsed(response=response, template_name="core/base.html")

    def test_resume_registers_visit(self):
        response: HttpResponse = self.client.get("/resume")

        self.assertEqual(first=Visit.objects.count(), second=1)


class MultiPageTest(TestCase):
    def test_visit_count(self):
        response: HttpResponse = self.client.get("/")
        response: HttpResponse = self.client.get("/contact")
        response: HttpResponse = self.client.get("/resume")

        self.assertEqual(first=Visit.objects.count(), second=3)
