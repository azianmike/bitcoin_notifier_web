# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submitAlertJSON', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='emailOrText',
        ),
        migrations.AddField(
            model_name='alert',
            name='emailAlert',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alert',
            name='textAlert',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
