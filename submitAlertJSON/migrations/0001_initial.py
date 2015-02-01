# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerJSON', '0002_auto_20150117_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('alertID', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('email', models.CharField(default=b'test', max_length=100)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('priceThreshold', models.IntegerField(default=b'12')),
                ('sign', models.CharField(default=b'12', max_length=20)),
                ('nextAlert', models.IntegerField(default=b'10')),
                ('intervalInSeconds', models.IntegerField(default=b'1000000')),
                ('emailAlert', models.BooleanField(default=False)),
                ('textAlert', models.BooleanField(default=False)),
                ('exchange', models.CharField(default=b'coinbase', max_length=100)),
                ('person', models.ForeignKey(to='registerJSON.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
