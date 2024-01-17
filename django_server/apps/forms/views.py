from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes , action
from rest_framework.response import Response
from reportlab.pdfgen import canvas
import io, os, re
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.files.base import ContentFile
from xhtml2pdf import pisa
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import (
    BookingRequest,
    CallBackRequest,
    Estimate,
    RecruitForm,
    Invoice,
    Maintenance,
    MaintenanceAgreementForm,
    Service,
    Repair,
    Install,
    Remodel,
    Routine
)
from .serializers import (
    BookingRequestSerializer,
    CallBackRequestSerializer,
    EstimateSerializer,
    RecruitFormSerializer,
    InvoiceSerializer,
    MaintenanceSerializer,
    MaintenanceAgreementFormSerializer,
    ServiceSerializer,
    RepairSerializer,
    InstallSerializer,
    RemodelSerializer,
    RoutineSerializer,
   
)





@authentication_classes([])  
@permission_classes([])
class ServiceListViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

@authentication_classes([])  
@permission_classes([])
class BookingRequestViewSet(viewsets.ModelViewSet):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer

    def send_email(self, instance):
        # Customize the email content as needed
        subject = 'New Booking Request'
        message = f'A new booking request has been received. Requested date: {instance.requested_date}'
        from_email = 'info@thepoolbuddy.com'
        recipient_list = [instance.email,'info@thepoolbuddy.com']  # Replace with the actual recipient(s)
        send_mail(subject, message, from_email, recipient_list)

    def perform_create(self, serializer):
        instance = serializer.save()
        
    
    def get_queryset(self):
        queryset = BookingRequest.objects.all()
        # You can add custom query parameters for filtering
        customer_email = self.request.query_params.get('customer_email', None)
        if customer_email:
            queryset = queryset.filter(customer_email=customer_email)
        # Add more filters as needed
        return queryset

@authentication_classes([])  
@permission_classes([])
class CallBackRequestViewSet(viewsets.ModelViewSet):
    queryset = CallBackRequest.objects.all()
    serializer_class = CallBackRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_email(instance)

    def get_queryset(self):
        queryset = CallBackRequest.objects.all()
        # You can add custom query parameters for filtering
        customer_email = self.request.query_params.get('customer_email', None)
        if customer_email:
            queryset = queryset.filter(customer_email=customer_email)
        # Add more filters as needed
        return queryset

    
    def send_email(self, instance):
        # Customize the email content as needed
        subject = 'We have scheduled your call'
        message = f'A new callback request has been received. Requested date of call: {instance.requested_date_of_call}'
        from_email = 'info@thepoolbuddy.com'
        recipient_list = [instance.email,'info@thepoolbuddy.com']  # Replace with the actual recipient(s)
        send_mail(subject, message, from_email, recipient_list)

@authentication_classes([])  
@permission_classes([])
class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_email(instance)

    def get_queryset(self):
        queryset = Estimate.objects.all()
        # You can add custom query parameters for filtering
        customer_email = self.request.query_params.get('customer_email', None)
        if customer_email:
            queryset = queryset.filter(customer_email=customer_email)
        # Add more filters as needed
        return queryset
        
    def send_email(self, instance):
        # Customize the email content as needed
        subject = 'New Estimate Request'
        message = f'A new estimate request has been received. Requested date: {instance.date_of_request}'
        from_email = 'info@thepoolbuddy.com'
        recipient_list = [instance.email,'info@thepoolbuddy.com']  # Replace with the actual recipient(s)
        send_mail(subject, message, from_email, recipient_list)

@authentication_classes([])  
@permission_classes([])
class RecruitFormViewSet(viewsets.ModelViewSet):
    queryset = RecruitForm.objects.all()
    serializer_class = RecruitFormSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_email(instance)
    
    def send_email(self, instance):
        # Customize the email content as needed
        subject = 'New Recruitment Form Submission'
        message = f'A new recruitment form has been submitted. Applicant: {instance.first_name},{instance.last_name} and we will call {instance.phone} within a couple of days.  Thank you.'
        from_email = 'info@thepoolbuddy.com'
        recipient_list = [instance.email,'info@thepoolbuddy.com']  # Replace with the actual recipient(s)
        send_mail(subject, message, from_email, recipient_list)

@authentication_classes([])  
@permission_classes([])
class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

    def get_queryset(self):
        queryset = Maintenance.objects.all()
        customer_email = self.request.query_params.get('customer_email', None)
        if customer_email:
            queryset = queryset.filter(customer_email=customer_email)
        # Add more custom filters as needed
        # Example: Get another custom query parameter
        custom_param = self.request.query_params.get('custom_param', None)
        if custom_param:
            queryset = queryset.filter(another_field=custom_param)

        # You can continue adding more filters based on your requirements

        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

@authentication_classes([])  
@permission_classes([])
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        # You can add custom query parameters for filtering
        customer_email = self.request.query_params.get('customer_email', None)
        if customer_email:
            queryset = queryset.filter(customer_email=customer_email)
        # Add more filters as needed
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

@authentication_classes([])  
@permission_classes([])
class MaintenanceAgreementFormViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceAgreementForm.objects.all()
    serializer_class = MaintenanceAgreementFormSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_email(instance)

    def generate_pdf(self, instance):
        # Read the template file
        template = get_template('Maintenance_Agreement.html')
        html = template.render({'instance': instance})

        # Generate PDF using xhtml2pdf
        result = io.BytesIO()
        pdf = pisa.CreatePDF(html, dest=result)

        if pdf.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        # Remove non-alphanumeric characters from phone number
        email_cleaned = re.sub(r'\W+', '', instance.email)

        # Save the PDF file with dynamic name
        file_name = f'agreements/maintenance_agreement_{email_cleaned}.pdf'
        file_path = default_storage.path(file_name)  # Specify the desired storage path

        # Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with default_storage.open(file_path, 'wb') as pdf_file:
            pdf_file.write(result.getvalue())

        return file_path


    def send_email(self, instance):
        subject = 'New Maintenance Agreement Form Submission'
        message = f'We recieved your maintnence agreement form that has been submitted.  From your submition we will email you a agreement you can sign then return to us to confirm maintenance. We will call {instance.phone} if we have any questions.'
        from_email = 'info@thepoolbuddy.com'
        recipient_list = [instance.email,'info@thepoolbuddy.com']  # Replace with the actual recipient(s)
        # Generate PDF
        pdf_path = self.generate_pdf(instance)

        # Create EmailMessage object
        email = EmailMessage(subject, message, from_email, recipient_list)
        dynamic_file_name = os.path.basename(pdf_path)
        # Attach PDF file to the email
        with open(pdf_path, 'rb') as pdf_file:
            email.attach(filename=dynamic_file_name, content=pdf_file.read(), mimetype='application/pdf')

        # Send the email
        email.send()

