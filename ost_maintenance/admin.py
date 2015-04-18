from django.contrib import admin
from .models import Machine, MaintenanceActivity, MachineUserType, MachineMaintenance
from .models import MachineMaintenanceActivity, MachineMaintenanceComment, MachineUser
from .models import MachineMaintenanceRequest, MachineMaintenanceRequestDetail


class MachineUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_type', 'first_name', 'last_name')
    list_filter = ['user_type',]


class MachineMaintenanceActivityInline(admin.TabularInline):
    model = MachineMaintenanceActivity
    extra = 3


class MachineMaintenanceCommentInline(admin.TabularInline):
    model = MachineMaintenanceComment
    extra = 1


class MachineMaintenanceAdmin(admin.ModelAdmin):
    inlines = [MachineMaintenanceActivityInline, MachineMaintenanceCommentInline]


class MachineMaintenanceRequestDetailInline(admin.TabularInline):
    model = MachineMaintenanceRequestDetail
    extra = 1


class MachineMaintenanceRequestAdmin(admin.ModelAdmin):
    inlines = [MachineMaintenanceRequestDetailInline]

admin.site.register(Machine)
admin.site.register(MaintenanceActivity)
admin.site.register(MachineUserType)
admin.site.register(MachineMaintenance, MachineMaintenanceAdmin)
admin.site.register(MachineUser, MachineUserAdmin)
admin.site.register(MachineMaintenanceRequest, MachineMaintenanceRequestAdmin)

