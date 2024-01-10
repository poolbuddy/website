from .models import Product, ProductWrapper, CustomerProductList
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductWrapperSerializer(serializers.ModelSerializer):
    product = ProductSerializer( read_only=True)
    class Meta:
        model = ProductWrapper
        fields = '__all__'
   
       
class CustomerProductListSerializer(serializers.ModelSerializer):
    product_list = ProductWrapperSerializer(many=True, read_only=True)
    class Meta:
        model = CustomerProductList
        fields = '__all__'

