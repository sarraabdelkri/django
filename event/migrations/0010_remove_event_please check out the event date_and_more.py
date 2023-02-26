# Generated by Django 4.1 on 2023-02-24 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0009_remove_event_please check out the event date_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="event", name="Please check out the event date",
        ),
        migrations.AddConstraint(
            model_name="event",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "evt_date__gte",
                        datetime.datetime(2023, 2, 24, 15, 57, 46, 226491),
                    )
                ),
                name="Please check out the event date",
            ),
        ),
    ]
