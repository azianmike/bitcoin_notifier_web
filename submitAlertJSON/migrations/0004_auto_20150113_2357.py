# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submitAlertJSON', '0003_alert_emailortext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='email_id',
            new_name='person',
        ),
    ]
