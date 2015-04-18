# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('netbios_name', models.CharField(unique=True, max_length=10, verbose_name=b'nombre de red')),
                ('workgroup', models.CharField(max_length=10, verbose_name=b'grupo de trabajo')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'activo')),
                ('create_dt', models.DateTimeField(verbose_name=b'fecha de alta')),
                ('withdrawal_dt', models.DateField(null=True, verbose_name=b'fecha de baja', blank=True)),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
        migrations.CreateModel(
            name='MachineMaintenance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schedule_dt', models.DateField(null=True, verbose_name=b'fecha programada', blank=True)),
                ('maintenance_dt', models.DateField(verbose_name=b'fecha de mantenimiento')),
                ('machine', models.ForeignKey(to='ost_maintenance.Machine')),
            ],
            options={
                'verbose_name': 'Mantenimiento de equipo',
                'verbose_name_plural': 'Mantenimientos de equipo',
            },
        ),
        migrations.CreateModel(
            name='MachineMaintenanceActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete', models.BooleanField(default=False)),
                ('comments', models.TextField(verbose_name=b'comentarios de mantenimiento')),
                ('machine_maintenance', models.ForeignKey(to='ost_maintenance.MachineMaintenance')),
            ],
            options={
                'verbose_name': 'Actividad de mantenimiento de equipo',
                'verbose_name_plural': 'Actividades de mantenimiento de equipo',
            },
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
            options={
                'verbose_name': 'Comentario de mantenimiento',
                'verbose_name_plural': 'Comentarios de mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='MachineMaintenanceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('format_c', models.BooleanField(default=False, verbose_name=b'formatear equipo')),
                ('machine', models.ForeignKey(to='ost_maintenance.Machine')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Petici\xf3n de mantenimiento',
                'verbose_name_plural': 'Peticiones de mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='MachineMaintenanceRequestDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_change_user', models.BooleanField(default=False, verbose_name=b'cambio de usuario')),
            ],
            options={
                'verbose_name': 'Detalle de petici\xf3n de mantenimiento',
                'verbose_name_plural': 'Detalle de peticiones de mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='MachineUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=75, verbose_name=b'usuario o email')),
                ('user_pass', models.CharField(max_length=15, null=True, verbose_name=b'contrase\xc3\xb1a', blank=True)),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name=b'nombre', blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name=b'apellidos', blank=True)),
                ('job', models.CharField(max_length=50, null=True, verbose_name=b'puesto', blank=True)),
                ('network_permissions', models.TextField(verbose_name=b'permisos de red')),
                ('is_active', models.BooleanField(default=True)),
                ('create_dt', models.DateField(verbose_name=b'fecha de alta')),
                ('withdrawal_dt', models.DateField(null=True, verbose_name=b'fecha de baja', blank=True)),
                ('machine', models.ForeignKey(to='ost_maintenance.Machine')),
            ],
            options={
                'verbose_name': 'Usuario de equipo',
                'verbose_name_plural': 'Usuarios de equipo',
            },
        ),
        migrations.CreateModel(
            name='MachineUserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.CharField(unique=True, max_length=25, verbose_name=b'tipo de usuario')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo de usuario',
                'verbose_name_plural': 'Tipos de usuario',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.CharField(unique=True, max_length=255, verbose_name=b'actividad')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'activo')),
            ],
            options={
                'verbose_name': 'Activiad de mantenimiento',
                'verbose_name_plural': 'Actividades de mantenimiento',
            },
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
            model_name='machinemaintenanceactivity',
            name='maintenance_activity',
            field=models.ForeignKey(to='ost_maintenance.MaintenanceActivity'),
        ),
        migrations.AddField(
            model_name='machinemaintenanceactivity',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
