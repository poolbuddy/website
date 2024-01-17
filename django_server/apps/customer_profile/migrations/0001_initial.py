# Generated by Django 4.2.8 on 2023-12-31 00:21

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraPoolEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceExtras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_type', models.CharField(max_length=255)),
                ('above_shape', models.CharField(blank=True, default='', max_length=255)),
                ('above_size', models.CharField(blank=True, default='', max_length=255)),
                ('inground_size', models.CharField(blank=True, default='', max_length=255)),
                ('inground_shape', models.CharField(blank=True, default='', max_length=255)),
                ('filter_type', models.CharField(blank=True, max_length=255)),
                ('sanitizer_type', models.CharField(blank=True, null=True)),
                ('pump_num', models.IntegerField(blank=True, null=True)),
                ('skimmer_num', models.IntegerField(blank=True, null=True)),
                ('main_drain_num', models.IntegerField(blank=True, null=True)),
                ('return_num', models.IntegerField(blank=True, null=True)),
                ('floor_return_num', models.IntegerField(blank=True, null=True)),
                ('pool_conditions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), null=True, size=None)),
                ('pool_extra_equipment', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), null=True, size=None)),
                ('comments', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoolConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodicity', models.CharField(choices=[('NA', 'NA'), ('W', 'Weekly'), ('B', 'Biweekly'), ('M', 'Monthly')], max_length=2)),
                ('chosen_plan', models.CharField(choices=[('N', 'None'), ('V', 'Value'), ('CO', 'Concierge'), ('CU', 'Custom')], max_length=2)),
                ('day_of_service', models.CharField(choices=[('NA', 'NA'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wensday'), ('TH', 'Thursday'), ('FR', 'Friday')], default='NA', max_length=2)),
                ('includes_chemicals', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('maintenance_extra_list', models.ManyToManyField(blank=True, to='customer_profile.maintenanceextras')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('last_login_array', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), null=True, size=None)),
                ('hasMembership', models.BooleanField(default=False)),
                ('store_credit', models.IntegerField(default=0)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_profile.address')),
                ('maintenance_aggreement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer_profile.maintenanceagreement')),
                ('pool_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_profile.pool')),
                ('product_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customerproductlist')),
            ],
        ),
    ]
