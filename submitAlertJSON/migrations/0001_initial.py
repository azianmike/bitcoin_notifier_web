# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerJSON', '0004_auto_20150106_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('email_test', models.CharField(default=b'test', max_length=100)),
                ('email_id', models.ForeignKey(primary_key=True, serialize=False, to='registerJSON.Person')),
                ('phone', models.CharField(default=b'123', max_length=20)),
                ('priceThreshold', models.IntegerField(default=b'12')),
                ('sign', models.CharField(default=b'12', max_length=20)),
                ('lastAlert', models.DateField(default=b'12', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
