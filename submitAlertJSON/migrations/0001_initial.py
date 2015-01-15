# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerJSON', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('email', models.CharField(default=b'test', max_length=100)),
                ('person', models.ForeignKey(primary_key=True, serialize=False, to='registerJSON.Person')),
                ('phone', models.CharField(max_length=20, null=True)),
                ('priceThreshold', models.IntegerField(default=b'12')),
                ('sign', models.CharField(default=b'12', max_length=20)),
                ('lastAlert', models.DateField(null=True, blank=True)),
                ('intervalInSeconds', models.IntegerField(default=b'1000000')),
                ('emailOrText', models.CharField(default=b'email', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
