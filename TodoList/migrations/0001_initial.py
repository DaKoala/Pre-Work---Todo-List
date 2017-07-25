# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('prior', models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('expire_date', models.DateField()),
                ('is_finished', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ToDo',
            },
        ),
    ]
