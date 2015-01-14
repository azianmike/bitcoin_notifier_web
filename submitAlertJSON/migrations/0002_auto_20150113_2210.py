# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submitAlertJSON', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='email_test',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='alert',
            name='phone',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
