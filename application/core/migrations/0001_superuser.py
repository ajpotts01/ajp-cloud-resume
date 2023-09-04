import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps

import google.auth
from google.cloud import secretmanager


# https://cloud.google.com/python/django/run#superuser_creation_with_data_migrations
def create_super_user(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    if os.getenv("TRAMPOLINE_CI", None) or settings.DEBUG or settings.TESTING:
        admin_password: str = "test"
    else:
        client: secretmanager.SecretManagerServiceClient = (
            secretmanager.SecretManagerServiceClient()
        )

        _, project = google.auth.default()

        PW_NAME: str = os.getenv("PW_NAME")
        secret_name: str = f"projects/{project}/secrets/{PW_NAME}/versions/latest"
        admin_password: str = client.access_secret_version(
            name=secret_name
        ).payload.data.decode("UTF-8")

    User.objects.create_superuser("admin", password=admin_password.strip())


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.RunPython(create_super_user)]
