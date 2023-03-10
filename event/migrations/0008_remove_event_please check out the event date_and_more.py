# Generated by Django 4.1 on 2023-02-20 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_remove_event_please check out the event date_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='event',
            name='Please check out the event date',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gte', datetime.datetime(2023, 2, 20, 11, 29, 8, 808592))), name='Please check out the event date'),
        ),
    ]
