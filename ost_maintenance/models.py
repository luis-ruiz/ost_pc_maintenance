# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Machine(models.Model):
    netbios_name = models.CharField('nombre de red', unique=True, null=False, blank=False, max_length=10)
    workgroup = models.CharField('grupo de trabajo', null=False, blank=False, max_length=10)
    is_active = models.BooleanField('activo', default=True)
    create_dt = models.DateTimeField('fecha de alta', null=False, blank=False)
    withdrawal_dt = models.DateField('fecha de baja', null=True, blank=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.netbios_name


class MaintenanceActivity(models.Model):
    activity = models.CharField('actividad', unique=True, null=False, blank=False, max_length=255)
    is_active = models.BooleanField('activo', default=True)

    class Meta:
        verbose_name = 'Activiad de mantenimiento'
        verbose_name_plural = 'Actividades de mantenimiento'

    def __unicode__(self):
        return self.activity


class MachineUserType(models.Model):
    user_type = models.CharField('tipo de usuario', unique=True, max_length=25)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tipo de usuario'
        verbose_name_plural = 'Tipos de usuario'

    def __str__(self):
        return self.user_type


class MachineMaintenance(models.Model):
    machine = models.ForeignKey(Machine)
    schedule_dt = models.DateField('fecha programada', null=True, blank=True)
    maintenance_dt = models.DateField('fecha de mantenimiento')

    class Meta:
        verbose_name = 'Mantenimiento de equipo'
        verbose_name_plural = 'Mantenimientos de equipo'


class MachineMaintenanceActivity(models.Model):
    machine_maintenance = models.ForeignKey(MachineMaintenance)
    maintenance_activity = models.ForeignKey(MaintenanceActivity)
    complete = models.BooleanField(default=False)
    comments = models.TextField('comentarios de mantenimiento')
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Actividad de mantenimiento de equipo'
        verbose_name_plural = 'Actividades de mantenimiento de equipo'


class MachineMaintenanceComment(models.Model):
    machine_maintenance = models.ForeignKey(MachineMaintenance)
    comment = models.TextField()
    is_improvement = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    approver_user = models.ForeignKey(User, null=True, blank=True, related_name='approver_user')

    class Meta:
        verbose_name = 'Comentario de mantenimiento'
        verbose_name_plural = 'Comentarios de mantenimiento'


class MachineUser(models.Model):
    machine = models.ForeignKey(Machine)
    user_type = models.ForeignKey(MachineUserType)
    username = models.CharField('usuario o email', unique=True, max_length=75)
    user_pass = models.CharField('contraseña', null=True, blank=True, max_length=15)
    first_name = models.CharField('nombre', null=True, blank=True, max_length=50)
    last_name = models.CharField('apellidos', null=True, blank=True, max_length=100)
    job = models.CharField('puesto', null=True, blank=True, max_length=50)
    network_permissions = models.TextField('permisos de red')
    is_active = models.BooleanField(default=True)
    create_dt = models.DateField('fecha de alta')
    withdrawal_dt = models.DateField('fecha de baja', null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario de equipo'
        verbose_name_plural = 'Usuarios de equipo'


class MachineMaintenanceRequest(models.Model):
    machine = models.ForeignKey(Machine)
    format_c = models.BooleanField('formatear equipo', default=False)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Petición de mantenimiento'
        verbose_name_plural = 'Peticiones de mantenimiento'


class MachineMaintenanceRequestDetail(models.Model):
    machine_maintenance_request = models.ForeignKey(MachineMaintenanceRequest)
    machine_user = models.ForeignKey(MachineUser, null=True, blank=True, related_name='machine_user')
    network_user = models.ForeignKey(MachineUser, null=True, blank=True, related_name='network_user')
    email_user = models.ForeignKey(MachineUser, null=True, blank=True, related_name='email_user')
    is_change_user = models.BooleanField('cambio de usuario', default=False)

    class Meta:
        verbose_name = 'Detalle de petición de mantenimiento'
        verbose_name_plural = 'Detalle de peticiones de mantenimiento'