# Generated by Django 3.2.10 on 2021-12-12 23:56

import django.db.models.deletion
import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models

import backend.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.CITIES_CITY_MODEL),
        ("backend", "0002_postgis"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "transactional_id",
                    models.CharField(
                        db_index=True,
                        default=backend.utils.generate_id,
                        editable=False,
                        max_length=30,
                        unique=True,
                    ),
                ),
                ("start", models.DateField()),
                ("end", models.DateField()),
                ("notes", models.TextField(blank=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.CITIES_CITY_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trips",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "transactional_id",
                    models.CharField(
                        db_index=True,
                        default=backend.utils.generate_id,
                        editable=False,
                        max_length=30,
                        unique=True,
                    ),
                ),
                ("distance", models.IntegerField(blank=True, default=None, null=True)),
                ("overlap_start", models.DateField()),
                ("overlap_end", models.DateField(blank=True, null=True)),
                (
                    "source_trip",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_matches",
                        to="backend.trip",
                    ),
                ),
                (
                    "source_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_matches",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "target_trip",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="target_matches",
                        to="backend.trip",
                    ),
                ),
                (
                    "target_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="target_matches",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("source_trip", "target_trip")},
            },
        ),
    ]
