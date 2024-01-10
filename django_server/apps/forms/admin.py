from django.contrib import admin
from .models import (
    Repair, 
    Install, 
    Remodel, 
    Routine, 
    BookingRequest, 
    CallBackRequest, 
    Estimate, 
    RecruitForm, 
    Invoice, 
    ChemicalConsumption, 
    MaintenanceExtras, 
    Maintenance,
    Service,
    MaintenanceAgreementForm)
# Register your models here.
admin.site.register(MaintenanceAgreementForm)
admin.site.register(Service)
admin.site.register(Repair)
admin.site.register(Install)
admin.site.register(Remodel)
admin.site.register(Routine)
admin.site.register(BookingRequest)
admin.site.register(CallBackRequest)
admin.site.register(Estimate)
admin.site.register(RecruitForm)
admin.site.register(Invoice)
admin.site.register(ChemicalConsumption)
admin.site.register(MaintenanceExtras)
admin.site.register(Maintenance)

