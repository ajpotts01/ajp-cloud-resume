# Generated by Django 4.2.4 on 2023-09-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_certification_education_job_skill_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="end_date",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="job",
            name="start_date",
            field=models.CharField(max_length=100),
        ),
    ]