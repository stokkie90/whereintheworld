# Generated by Django 3.2.10 on 2022-01-21 00:50

from django.db import migrations, models

import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_match_trip"),
    ]

    operations = [
        migrations.AddField(
            model_name="match",
            name="are_meeting",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name="match",
            name="source_state",
            field=models.CharField(
                choices=[("unseen", "Unseen"), ("seen", "Seen"), ("dismissed", "Dismissed")],
                default="unseen",
                max_length=24,
            ),
        ),
        migrations.AddField(
            model_name="match",
            name="target_state",
            field=models.CharField(
                choices=[("unseen", "Unseen"), ("seen", "Seen"), ("dismissed", "Dismissed")],
                default="unseen",
                max_length=24,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="work_hours",
            field=models.JSONField(
                blank=True,
                default=None,
                null=True,
                validators=[
                    backend.validators.JSONValidator(
                        {
                            "$schema": "http://json-schema.org/draft-07/schema#",
                            "additionalProperties": False,
                            "properties": {"end": {"type": "string"}, "start": {"type": "string"}},
                            "required": ["start", "end"],
                            "type": "object",
                        }
                    )
                ],
            ),
        ),
    ]