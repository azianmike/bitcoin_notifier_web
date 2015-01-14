# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submitAlertJSON', '0002_auto_20150113_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='emailOrText',
            field=models.CharField(default=b'email', max_length=50),
            preserve_default=True,
        ),
    ]
