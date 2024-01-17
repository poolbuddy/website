from django.db import models
from django.contrib.postgres.fields import ArrayField
from meta.models import ModelMeta

class Service(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Repair(Service):
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}"
        
class Install(Service):
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}"

class Remodel(Service):
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}"

class Routine(Service):
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}"

class Estimate(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    services_of_interest = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_sent = models.DateField(blank=True, null=True)
    time_of_day = models.CharField(max_length=255, blank=True, null=True)
    sent_confirm_text = models.BooleanField(default=False)
    picture_1 = models.ImageField(upload_to='estimate_images/', default='estimate_images/image.jpg', blank=True)
    picture_2 = models.ImageField(upload_to='estimate_images/', default='estimate_images/image.jpg', blank=True)
    picture_3 = models.ImageField(upload_to='estimate_images/', default='estimate_images/image.jpg', blank=True)

    def __str__(self):
        return f"{self.email}"

class BookingRequest(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    services_of_interest = ArrayField(models.CharField(max_length=255))
    urgency = models.CharField(max_length=255,blank=True, null=True)
    appt_flexibility = models.CharField(max_length=255, blank=True, null=True)
    someone_willB_home = models.BooleanField(default=False) 
    requests_a_time_of_day = models.BooleanField(default=False)  
    requested_date = models.DateField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    requested_time_of_day = models.CharField(max_length=255, blank=True, null=True)
    has_attached_estimate = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    confirmed_date = models.DateField(blank=True, null=True)
    attached_estimate = models.ForeignKey(Estimate, blank=True, null=True ,on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.email}"

class MaintenanceAgreementForm(models.Model):
    email = models.CharField(max_length=255, null=True, blank=True) 
    phone = models.CharField(max_length=255, null=True, blank=True) 
    frequency_of_service = models.CharField(max_length=255)                                            
    insurance_understand = models.BooleanField()
    equipment_comments = models.TextField()
    equipment_understand = models.BooleanField()
    access_comments = models.TextField()
    equipment_is_good = models.BooleanField()
    there_is_access = models.BooleanField()
    responsibility_comments = models.TextField()
    pump_settings_understand_2 = models.BooleanField()
    access_understand = models.BooleanField()
    pump_settings_understand_1 = models.BooleanField()
    leak_chemical_understand = models.BooleanField()
    understand_termination = models.BooleanField()
    bundled_maintenance_plan = models.BooleanField()
    check_payment_extra_pref = models.CharField(max_length=255)
    prefered_payment_method = models.CharField(max_length=255)
    end_date = models.DateField()
    start_date = models.DateField()
    alternate_service_day_preference = models.CharField(max_length=255)
    weather_delay_preference = models.CharField(max_length=255)
    communication_comments = models.TextField()
    preferred_communication_method = models.CharField(max_length=255)
    select_extras = models.CharField(max_length=255)
    select_scope = models.CharField(max_length=255)

class CallBackRequest(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    requested_date_of_call = models.DateField(auto_now=True)
    time_of_day = models.CharField(max_length=255, blank=True, null=True)
    call_asap = models.BooleanField(default=False)
    confirmed =  models.BooleanField(default=False)
    confirm_text = models.BooleanField(default=False)
    services_of_interest = ArrayField(models.CharField(max_length=255))

    def __str__(self):
        return f"{self.customer_email}"
        
class RecruitForm(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    has_drivers_license = models.BooleanField( null=True, blank=True)
    has_vehicle = models.BooleanField( null=True, blank=True)
    vehicle_has_hitch = models.BooleanField( null=True, blank=True)
    desired_responsibilities = ArrayField(models.CharField(max_length=255), null=True)
    has_general_experience = models.BooleanField(null=True,blank=True)
    has_pro_experience = models.BooleanField(null=True,blank=True)
    years_of_experience = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name}"


class Invoice(models.Model):
    charge = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    qb_invoice_number = models.CharField(null=True, blank=True)
    service_list = models.ManyToManyField(Service)
    date_of_service = models.DateField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    received_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.email} - {self.qb_invoice_number}"


class ChemicalConsumption(models.Model):
    chemical = models.CharField(max_length=255)
    amount = models.CharField(max_length=255,null=True, blank=True)
    customers_chemicals = models.BooleanField(null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.chemical}"

class MaintenanceExtras(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Maintenance(models.Model):
    email = models.EmailField()
    date_performed = models.DateField(null=True, blank=True)
    before_picture = models.ImageField(upload_to='maintenance/',default='maintenance/image.jpg', blank=True)
    after_picture = models.ImageField(upload_to='maintenance/',default='maintenance/image.jpg', blank=True)
    weather_delay = models.BooleanField(default=False)
    optional_additions = models.ManyToManyField(MaintenanceExtras, blank=True)
    chemical_consumption = models.ManyToManyField(ChemicalConsumption, blank=True)

    def __str__(self):
        return f"{self.email}"
