# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerJSON', '0003_auto_20150106_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
