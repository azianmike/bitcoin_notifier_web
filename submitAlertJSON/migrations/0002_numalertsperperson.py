# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerJSON', '0002_auto_20150117_0140'),
        ('submitAlertJSON', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumAlertsPerPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numAlerts', models.IntegerField(default=0)),
                ('maxAlerts', models.IntegerField(default=1)),
                ('person', models.ForeignKey(to='registerJSON.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
