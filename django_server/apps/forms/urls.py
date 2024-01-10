from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookingRequestViewSet, 
    CallBackRequestViewSet,
    EstimateViewSet, 
    RecruitFormViewSet, 
    MaintenanceViewSet, 
    InvoiceViewSet,
    MaintenanceAgreementFormViewSet,
    ServiceListViewSet)

router = DefaultRouter()
router.register(r'service_list', ServiceListViewSet)
router.register(r'maintenance_agreement', MaintenanceAgreementFormViewSet)
router.register(r'maintenance', MaintenanceViewSet, basename='maintenance')
router.register(r'invoice', InvoiceViewSet, basename='invoice')
router.register(r'booking_request', BookingRequestViewSet, basename='booking_request')
router.register(r'estimate', EstimateViewSet, basename='estimate')
router.register(r'call_back', CallBackRequestViewSet, basename='call_back')
router.register(r'hiring_form', RecruitFormViewSet, basename='hiring_form')

urlpatterns = [
  
]+ router.urls
