from django.shortcuts import render
from rest_framework import viewsets, serializers 
from .models import Product, ProductWrapper, CustomerProductList
from rest_framework import status, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import ProductSerializer, ProductWrapperSerializer, CustomerProductListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes, permission_classes 
from datetime import datetime
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import viewsets, status
from django.core.mail import send_mail

@authentication_classes([])  
@permission_classes([])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductWrapper.objects.all()
    serializer_class = ProductWrapperSerializer
    
    @action(detail=True, methods=['POST'])
    def order_product(self, request):
    # Your existing code
       return

    def get_queryset(self):
        queryset = super().get_queryset()

        email = self.request.query_params.get('email', None)
        paid = self.request.query_params.get('paid', None)
        delivered = self.request.query_params.get('delivered', None)
        ordered = self.request.query_params.get('ordered', None)
        
        queryset = queryset.filter(customer_email=email)
     
        if paid:
            queryset = queryset.filter(paid=paid)

        if delivered:
            queryset = queryset.filter(delivered=delivered)
            
        return queryset

    
        
    def perform_create(self, serializer):

        customer_email = self.request.data.get('customer_email', None)
        speed = self.request.data.get('speed', None)
        delivery_type = self.request.data.get('delivery_type', None)
        payment_method = self.request.data.get('payment_method', None)
        product = self.request.data.get('product', None)
        quantity = self.request.data.get('quantity', None)
        try:
            product_instance = Product.objects.get(id=1)
            instance = ProductWrapper.objects.create(
                delivery_type=delivery_type,
                customer_email=customer_email,
                product=product_instance,
                payment_method=payment_method,
                quantity=quantity,
                speed=speed
                
            )
            print(instance)
            serializer = self.get_serializer(instance, data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # send email
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        except ProductWrapper.DoesNotExist:
            return Response({'error': 'Object not found'}, status=404)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def send_email(self, instance):
        # Customize the email content as needed
        subject = 'New Recruitment Form Submission'
        message = f'A new recruitment form has been submitted. Applicant: {instance.first_name} {instance.last_name}'
        from_email = 'you@example.com'
        recipient_list = ['you@example.com']  # Replace with the actual recipient(s)
        send_mail(subject, message, from_email, recipient_list)

@authentication_classes([])  
@permission_classes([])
class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

   

@authentication_classes([])  
@permission_classes([])
class CustomerProductListView(viewsets.ModelViewSet):
    queryset = CustomerProductList.objects.all()
    serializer_class = CustomerProductListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def add_item(self, request):
        print(self.request.data)
        email = self.request.data.get('email', None)
        product = self.request.data.get('product', None)
        speed = self.request.data.get('speed', None)
        delivery_type = self.request.data.get('delivery_type', None)
        quantity = self.request.data.get('quantity', None)
        payment_method = self.request.data.get('payment_method', None)
        payment = self.request.data.get('payment', None)
        try:
            product_instance = Product.objects.get(id=product)
            wrapper = ProductWrapper.objects.create(
                delivery_type=delivery_type,
                customer_email=email,
                product=product_instance,
                payment_method=payment_method,
                quantity=quantity,
                speed=speed
            )
            # Try to get the existing CustomerProductList
            instance = CustomerProductList.objects.get(email=email)

            # Add the wrapper to the product list
            instance.product.add(wrapper)

            serializer = CustomerProductListSerializer(instance)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        except CustomerProductList.DoesNotExist:
            return Response({'error': 'CustomerProductList not found'}, status=404)
