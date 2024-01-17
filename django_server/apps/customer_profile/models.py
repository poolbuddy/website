from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import date
from apps.store.models import CustomerProductList


class ExtraPoolEquipment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class PoolConditions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class MaintenanceExtras(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class MaintenanceAgreement(models.Model):

    DAYS_OF_WEEK = [
        ('NA', 'NA'),
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wensday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday')
    ]

    PERIODICITY_CHOICES = [
        ('NA', 'NA'),
        ('W', 'Weekly'),
        ('B', 'Biweekly'),
        ('M', 'Monthly'),
    ]

    PLAN_CHOICES = [
        ('N', 'None'),
        ('V', 'Value'),
        ('CO', 'Concierge'),
        ('CU', 'Custom'),
    ]

    periodicity = models.CharField(max_length=2, choices=PERIODICITY_CHOICES)
    chosen_plan = models.CharField(max_length=2, choices=PLAN_CHOICES)
    day_of_service = models.CharField(max_length=2, choices=DAYS_OF_WEEK, default="NA")
    includes_chemicals = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    maintenance_extra_list = models.ManyToManyField(MaintenanceExtras, blank=True)

    def __str__(self):
        return f"{self.chosen_plan}"

class Address(models.Model):
    street = models.CharField(max_length=255)
    town= models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.town} + {self.street}"

class Pool(models.Model):
    pool_type = models.CharField(max_length=255)
    above_shape = models.CharField(max_length=255, default="", blank=True)
    above_size = models.CharField(max_length=255, default="",  blank=True)
    inground_size = models.CharField(max_length=255, default="", blank=True)
    inground_shape = models.CharField(max_length=255, default="",blank=True)
    filter_type = models.CharField(max_length=255, blank=True)
    sanitizer_type = models.CharField(null=True, blank=True)
    pump_num = models.IntegerField(null=True, blank=True)
    skimmer_num = models.IntegerField(null=True, blank=True)
    main_drain_num = models.IntegerField( null=True, blank=True)
    return_num = models.IntegerField( null=True, blank=True)
    floor_return_num = models.IntegerField( null=True, blank=True)
    pool_conditions = ArrayField(models.CharField(max_length=255, null=True, blank=True), null=True)
    pool_extra_equipment = ArrayField(models.CharField(max_length=255, null=True, blank=True), null=True)
    comments = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f"{self.pool_type} + {self.above_size} + {self.inground_size}"


class CustomerProfile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    last_login_array = ArrayField(models.DateField( null=True,blank=True), null=True)
    hasMembership = models.BooleanField(default=False)
    store_credit = models.IntegerField(default=0)
    maintenance_aggreement = models.ForeignKey(MaintenanceAgreement, null=True, blank=True, on_delete=models.DO_NOTHING)
    pool_data = models.ForeignKey(Pool, on_delete=models.CASCADE)
    product_list = models.ForeignKey(CustomerProductList, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def formatted_last_login(self):
        return self.last_login_array[self.last_login_array.size - 1].strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"{self.id}-{self.email}"

