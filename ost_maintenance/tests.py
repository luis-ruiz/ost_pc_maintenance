from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from ost_maintenance.models import Machine

# Create your tests here.


class MachineTest(TestCase):
    def test_create_machine(self):
        machine = Machine()

        machine.netbios_name = 'ALT_LAP001'
        machine.workgroup = 'Alterna'
        machine.is_active = True
        machine.create_dt = timezone.now()

        machine.save()

        all_machines = Machine.objects.all()
        self.assertEquals(len(all_machines), 1)
        only_machine = all_machines[0]
        self.assertEquals(only_machine, machine)

        self.assertEquals(only_machine.netbios_name, 'ALT_LAP001')
        self.assertEquals(only_machine.workgroup, 'Alterna')
        self.assertEquals(only_machine.create_dt.day, machine.create_dt.day)
        self.assertEquals(only_machine.create_dt.month, machine.create_dt.month)
        self.assertEquals(only_machine.create_dt.year, machine.create_dt.year)
        self.assertEquals(only_machine.create_dt.hour, machine.create_dt.hour)
        self.assertEquals(only_machine.create_dt.minute, machine.create_dt.minute)
        self.assertEquals(only_machine.create_dt.second, machine.create_dt.second)


class AdminTest(LiveServerTestCase):
    def test_login(self):
        c = Client()

        response = c.get('/admin/')

        self.assertEquals(response.status_code, 200)

        self.assertTrue('Log in' in response.content)

