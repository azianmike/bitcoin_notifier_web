# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('email', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256, null=True)),
                ('accountType', models.CharField(default=b'free', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
