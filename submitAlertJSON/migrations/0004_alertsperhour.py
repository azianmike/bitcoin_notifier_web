# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submitAlertJSON', '0003_auto_20150201_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertsPerHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastHour', models.IntegerField(default=0)),
                ('alertsSentInLastHour', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
