# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ost_maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'activo'),
        ),
        migrations.AddField(
            model_name='machine',
            name='withdrawal_dt',
            field=models.DateField(default=datetime.datetime(2015, 4, 14, 15, 46, 50, 89679, tzinfo=utc), verbose_name=b'fecha de baja'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machine',
            name='create_dt',
            field=models.DateTimeField(verbose_name=b'fecha de alta'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='netbios_name',
            field=models.CharField(max_length=10, verbose_name=b'nombre de red'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='workgroup',
            field=models.CharField(max_length=10, verbose_name=b'grupo de trabajo'),
        ),
    ]
