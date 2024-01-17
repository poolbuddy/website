from rest_framework import serializers
from .models import ExtraPoolEquipment, PoolConditions, MaintenanceAgreement, CustomerProfile, MaintenanceExtras, Pool, Address
from apps.store.models import CustomerProductList
from apps.store.serializers import CustomerProductListSerializer

class ExtraPoolEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraPoolEquipment
        fields = '__all__'

class MaintenanceExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceExtras
        fields = '__all__'

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PoolConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolConditions
        fields = '__all__'

class MaintenanceAgreementSerializer(serializers.ModelSerializer):
    maintenance_extra_list = MaintenanceExtrasSerializer(many=True, read_only=True)
    class Meta:
        model = MaintenanceAgreement
        fields = '__all__'

class CustomerProfileReadSerializer(serializers.ModelSerializer):
    maintenance_aggreement = MaintenanceAgreementSerializer(read_only=True)
    pool_data = PoolSerializer(read_only=True)
    product_list = CustomerProductListSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    class Meta:
        model = CustomerProfile
        fields = '__all__'


class CustomerProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'

    






   
