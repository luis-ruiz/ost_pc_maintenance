from django.contrib import admin
from .models import Machine, MaintenanceActivity, MachineUserType, MachineMaintenance
from .models import MachineMaintenanceActivity, MachineMaintenanceComment, MachineUser
from .models import MachineMaintenanceRequest, MachineMaintenanceRequestDetail, Customer


class CustomerAdmin(admin.ModelAdmin):
    model = Customer


class MachineUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_type', 'first_name', 'last_name')
    list_filter = ['user_type', ]


class MachineMaintenanceActivityInline(admin.TabularInline):
    model = MachineMaintenanceActivity
    extra = 3


class MachineMaintenanceCommentInline(admin.TabularInline):
    model = MachineMaintenanceComment
    extra = 1


class MachineMaintenanceAdmin(admin.ModelAdmin):
    ordering = ['machine', 'maintenance_dt']
    list_display = ('machine', 'maintenance_dt', 'schedule_dt')
    inlines = [MachineMaintenanceActivityInline, MachineMaintenanceCommentInline]


class MachineMaintenanceRequestDetailInline(admin.TabularInline):
    model = MachineMaintenanceRequestDetail
    extra = 1


class MachineMaintenanceRequestAdmin(admin.ModelAdmin):
    inlines = [MachineMaintenanceRequestDetailInline]

    def get_form(self, request, *args, **kwargs):
        form = super(MachineMaintenanceRequestAdmin, self).get_form(request, *args, **kwargs)
        form.base_fields['user'].initial = request.user
        return form

admin.site.register(Customer)
admin.site.register(Machine)
admin.site.register(MaintenanceActivity)
admin.site.register(MachineUserType)
admin.site.register(MachineMaintenance, MachineMaintenanceAdmin)
admin.site.register(MachineUser, MachineUserAdmin)
admin.site.register(MachineMaintenanceRequest, MachineMaintenanceRequestAdmin)

