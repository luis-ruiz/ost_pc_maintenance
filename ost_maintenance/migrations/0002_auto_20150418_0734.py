# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ost_maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenanceactivity',
            options={'verbose_name': 'Actividad de mantenimiento', 'verbose_name_plural': 'Actividades de mantenimiento'},
        ),
        migrations.AlterField(
            model_name='machineuser',
            name='network_permissions',
            field=models.TextField(null=True, verbose_name=b'permisos de red', blank=True),
        ),
        migrations.AlterField(
            model_name='machineuser',
            name='username',
            field=models.CharField(max_length=75, verbose_name=b'usuario o email'),
        ),
    ]
