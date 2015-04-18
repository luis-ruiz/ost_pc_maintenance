# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ost_maintenance', '0002_auto_20150418_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinemaintenance',
            name='maintenance_dt',
            field=models.DateField(null=True, verbose_name=b'fecha de mantenimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='machinemaintenanceactivity',
            name='comments',
            field=models.TextField(null=True, verbose_name=b'comentarios de mantenimiento', blank=True),
        ),
    ]
