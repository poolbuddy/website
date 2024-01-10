# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ExtraPoolEquipmentViewSet,
    PoolConditionsViewSet,
    MaintenanceAgreementViewSet,
    CustomerProfileViewSet,
    PoolViewSet,
    AddressViewSet,
    
)
router = DefaultRouter()
router.register(r'extra-pool-equipment', ExtraPoolEquipmentViewSet, basename='extra-pool-equipment')
router.register(r'pool-conditions', PoolConditionsViewSet, basename='pool-conditions')
router.register(r'maintenance-agreement', MaintenanceAgreementViewSet, basename='maintenance-agreement')
router.register(r'customer-profile', CustomerProfileViewSet)
router.register(r'pool', PoolViewSet, basename='pool')
router.register(r'address', AddressViewSet, basename='address')


urlpatterns = [
]+ router.urls