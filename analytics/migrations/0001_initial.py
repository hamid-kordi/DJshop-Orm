# Generated by Django 5.0.8 on 2024-09-10 13:05

import django.contrib.admin.models
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('admin.logentry',),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]
