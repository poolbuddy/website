from django.contrib import admin
from .models import ExtraPoolEquipment, PoolConditions, MaintenanceAgreement, CustomerProfile, Pool, Address
# Register your models here.
admin.site.register(ExtraPoolEquipment)
admin.site.register(PoolConditions)
admin.site.register(MaintenanceAgreement)
admin.site.register(CustomerProfile)
admin.site.register(Pool)
admin.site.register(Address)