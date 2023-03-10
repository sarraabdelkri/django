# Generated by Django 4.1 on 2023-02-06 10:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_alter_person_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0003_remove_event_please check out the event date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_participation', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='event',
            name='Please check out the event date',
        ),
        migrations.AddField(
            model_name='event',
            name='participant',
            field=models.ManyToManyField(related_name='participant', through='event.participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gte', datetime.datetime(2023, 2, 6, 11, 17, 10, 500716))), name='Please check out the event date'),
        ),
        migrations.AddField(
            model_name='participants',
            name='evenement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='participants',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
