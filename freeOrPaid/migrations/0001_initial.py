# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'free', max_length=100)),
                ('price', models.IntegerField(default=b'0')),
                ('numOfAlerts', models.IntegerField(default=b'1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
