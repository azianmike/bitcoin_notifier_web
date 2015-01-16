# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeOrPaid', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='id',
        ),
        migrations.AlterField(
            model_name='pricing',
            name='status',
            field=models.CharField(default=b'free', max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
