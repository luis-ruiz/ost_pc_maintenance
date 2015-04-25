from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from ost_maintenance.models import Customer, Machine


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'


class MachineResource(ModelResource):
    customer = fields.ForeignKey(CustomerResource, 'customer')

    class Meta:
        queryset = Machine.objects.all()
        resource_name = 'machine'
        authorization = Authorization()