from django.db import models

# Create your models here.
class Machine(models.Model):
    netbios_name = models.CharField(max_length=10)
    workgroup = models.CharField(max_length=10)
    create_dt = models.DateTimeField()