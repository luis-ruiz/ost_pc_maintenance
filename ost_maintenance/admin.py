from django.contrib import admin
from .models import Machine, MaintenanceActivity, MachineUserType, MachineMaintenance
from .models import MachineMaintenanceActivity, MachineMaintenanceComment, MachineUser
from .models import MachineMaintenanceRequest, MachineMaintenanceRequestDetail


admin.site.register(Machine)
admin.site.register(MaintenanceActivity)
admin.site.register(MachineUserType)
admin.site.register(MachineMaintenance)
admin.site.register(MachineMaintenanceActivity)
admin.site.register(MachineMaintenanceComment)
admin.site.register(MachineUser)
admin.site.register(MachineMaintenanceRequest)
admin.site.register(MachineMaintenanceRequestDetail)
