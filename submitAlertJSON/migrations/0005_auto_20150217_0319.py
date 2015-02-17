# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerJSON', '0002_auto_20150117_0140'),
        ('submitAlertJSON', '0004_alertsperhour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertsperhour',
            name='id',
        ),
        migrations.AddField(
            model_name='alertsperhour',
            name='person',
            field=models.ForeignKey(primary_key=True, default=1, serialize=False, to='registerJSON.Person'),
            preserve_default=False,
        ),
    ]
