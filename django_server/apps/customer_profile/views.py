from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes , action
from django.utils import timezone
from django.shortcuts import get_object_or_404
from apps.store.models import CustomerProductList
from .models import ExtraPoolEquipment, PoolConditions, MaintenanceAgreement, CustomerProfile, Pool, Address
from .serializers import (
    ExtraPoolEquipmentSerializer,
    PoolConditionsSerializer,
    MaintenanceAgreementSerializer,
    CustomerProfileReadSerializer,
    CustomerProfileWriteSerializer,
    PoolSerializer,
    AddressSerializer
    
)
@authentication_classes([])  
@permission_classes([])
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance

@authentication_classes([])  
@permission_classes([])
class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance
@authentication_classes([])  
@permission_classes([])
class ExtraPoolEquipmentViewSet(viewsets.ModelViewSet):
    queryset = ExtraPoolEquipment.objects.all()
    serializer_class = ExtraPoolEquipmentSerializer

@authentication_classes([])  
@permission_classes([])
class PoolConditionsViewSet(viewsets.ModelViewSet):
    queryset = PoolConditions.objects.all()
    serializer_class = PoolConditionsSerializer

@authentication_classes([])  
@permission_classes([])
class MaintenanceAgreementViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceAgreement.objects.all()
    serializer_class = MaintenanceAgreementSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        
    def send_email(self, instance):
        # Customize the email content as needed
        subject = 'New Booking Request'
        message = f'A new booking request has been received. Requested date: {instance}'
        from_email = 'you@example.com'
        recipient_list = ['you@example.com']  # Replace with the actual recipient(s)
        send_mail(subject, message, from_email, recipient_list)
        
    @action(detail=False, methods=['GET'])
    def get_by_email(self, request):
        email = request.query_params.get('email', None)
        if email is None:
            return Response({'error': 'Email parameter is required'}, status=400)

        try:
            instance = YourModel.objects.get(email=email)
            serializer = YourModelSerializer(instance)
            return Response(serializer.data)
        except YourModel.DoesNotExist:
            return Response({'error': 'Object not found'}, status=404)

        
@authentication_classes([])  
@permission_classes([])
class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()


    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CustomerProfileReadSerializer
        return CustomerProfileWriteSerializer
 
    def perform_create(self, serializer):
        instance = serializer.save()
       
        return instance

       
    def send_email(self, instance):
        # Customize the email content as needed
        subject = 'New Profile Made'
        message = f'A new profile was made by: {instance.email}'
        from_email = 'info@poolbuddy.com'
        recipient_list = ['info@poolbuddy.com']  # Replace with the actual recipient(s)
        send_mail(subject, message, from_email, recipient_list)

    @action(detail=True, methods=['PUT'])
    def update_last_login(self, request, pk, *args, **kwargs):
        # Retrieve the customer profile object
        customer_profile = get_object_or_404(CustomerProfile, id=pk)
        # Update the last login array
        customer_profile.last_login_array.append(timezone.now())
        customer_profile.save()
        return Response({'success': 'date parameter is added'}, status=200)