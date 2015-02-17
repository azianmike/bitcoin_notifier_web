# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submitAlertJSON', '0002_numalertsperperson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numalertsperperson',
            name='id',
        ),
        migrations.AlterField(
            model_name='numalertsperperson',
            name='person',
            field=models.ForeignKey(primary_key=True, serialize=False, to='registerJSON.Person'),
            preserve_default=True,
        ),
    ]
