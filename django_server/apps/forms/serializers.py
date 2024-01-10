from rest_framework import serializers
from .models import (
    BookingRequest,
    CallBackRequest,
    Estimate,
    RecruitForm,
    Invoice,
    ChemicalConsumption,
    MaintenanceExtras,
    Maintenance,
    MaintenanceAgreementForm,
    Service,
    Repair,
    Install,
    Remodel,
    Routine
)





class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'
class RepairSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repair
        fields = '__all__'
class InstallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Install
        fields = '__all__'

class RemodelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Remodel
        fields = '__all__'

       
class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = '__all__'

class MaintenanceAgreementFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceAgreementForm
        fields = '__all__'

class BookingRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingRequest
        fields = '__all__'

class CallBackRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallBackRequest
        fields = '__all__'

class EstimateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estimate
        fields = '__all__'

class RecruitFormSerializer(serializers.ModelSerializer):
    desired_responsibilities = serializers.ListField(
        child=serializers.CharField(max_length=255), allow_null=True
    )

    class Meta:
        model = RecruitForm
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    service_list = serializers.StringRelatedField(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'

class ChemicalConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalConsumption
        fields = '__all__'

class MaintenanceExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceExtras
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    optional_additions = MaintenanceExtrasSerializer(many=True, read_only=True)
    chemical_consumption = ChemicalConsumptionSerializer(many=True, read_only=True)

    class Meta:
        model = Maintenance
        fields = '__all__'