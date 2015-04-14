# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ost_maintenance', '0002_auto_20150414_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineMaintenance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schedule_dt', models.DateField(null=True, verbose_name=b'fecha programada', blank=True)),
                ('maintenance_dt', models.DateField(verbose_name=b'fecha de mantenimiento')),
            ],
        ),
        migrations.CreateModel(
            name='MachineMaintenanceActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete', models.BooleanField(default=False)),
                ('comments', models.TextField(verbose_name=b'comentarios de mantenimiento')),
                ('machine_maintenance', models.ForeignKey(to='ost_maintenance.MachineMaintenance')),
            ],
        ),
        migrations.CreateModel(
            name='MachineMaintenanceComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('is_improvement', models.BooleanField(default=True)),
                ('approved', models.BooleanField(default=False)),
                ('approver_user', models.ForeignKey(related_name='approver_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('machine_maintenance', models.ForeignKey(to='ost_maintenance.MachineMaintenance')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MachineMaintenanceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('format_c', models.BooleanField(default=False, verbose_name=b'formatear equipo')),
            ],
        ),
        migrations.CreateModel(
            name='MachineMaintenanceRequestDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_change_user', models.BooleanField(default=False, verbose_name=b'cambio de usuario')),
            ],
        ),
        migrations.CreateModel(
            name='MachineUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=75, verbose_name=b'usuario o email')),
                ('user_pass', models.CharField(max_length=15, null=True, verbose_name=b'contrase\xc3\xb1a', blank=True)),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name=b'nombre', blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name=b'apellidos', blank=True)),
                ('job', models.CharField(max_length=50, null=True, verbose_name=b'puesto', blank=True)),
                ('network_permissions', models.TextField(verbose_name=b'permisos de red')),
                ('is_active', models.BooleanField(default=True)),
                ('create_dt', models.DateField(verbose_name=b'fecha de alta')),
                ('withdrawal_dt', models.DateField(null=True, verbose_name=b'fecha de baja', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MachineUserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.CharField(max_length=25, verbose_name=b'tipo de usuario')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.CharField(max_length=255, verbose_name=b'actividad')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'activo')),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='withdrawal_dt',
            field=models.DateField(null=True, verbose_name=b'fecha de baja', blank=True),
        ),
        migrations.AddField(
            model_name='machineuser',
            name='machine',
            field=models.ForeignKey(to='ost_maintenance.Machine'),
        ),
        migrations.AddField(
            model_name='machineuser',
            name='user_type',
            field=models.ForeignKey(to='ost_maintenance.MachineUserType'),
        ),
        migrations.AddField(
            model_name='machinemaintenancerequestdetail',
            name='email_user',
            field=models.ForeignKey(related_name='email_user', blank=True, to='ost_maintenance.MachineUser', null=True),
        ),
        migrations.AddField(
            model_name='machinemaintenancerequestdetail',
            name='machine_maintenance_request',
            field=models.ForeignKey(to='ost_maintenance.MachineMaintenanceRequest'),
        ),
        migrations.AddField(
            model_name='machinemaintenancerequestdetail',
            name='machine_user',
            field=models.ForeignKey(related_name='machine_user', blank=True, to='ost_maintenance.MachineUser', null=True),
        ),
        migrations.AddField(
            model_name='machinemaintenancerequestdetail',
            name='network_user',
            field=models.ForeignKey(related_name='network_user', blank=True, to='ost_maintenance.MachineUser', null=True),
        ),
        migrations.AddField(
            model_name='machinemaintenancerequest',
            name='machine',
            field=models.ForeignKey(to='ost_maintenance.Machine'),
        ),
        migrations.AddField(
            model_name='machinemaintenancerequest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='machinemaintenanceactivity',
            name='maintenance_activity',
            field=models.ForeignKey(to='ost_maintenance.MaintenanceActivity'),
        ),
        migrations.AddField(
            model_name='machinemaintenanceactivity',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='machinemaintenance',
            name='machine',
            field=models.ForeignKey(to='ost_maintenance.Machine'),
        ),
    ]
