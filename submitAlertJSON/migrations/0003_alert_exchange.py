# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submitAlertJSON', '0002_auto_20150118_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='exchange',
            field=models.CharField(default=b'coinbase', max_length=100),
            preserve_default=True,
        ),
    ]
