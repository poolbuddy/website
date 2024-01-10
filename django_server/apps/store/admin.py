from django.contrib import admin
from .models import Product, ProductWrapper, CustomerProductList

admin.site.register(Product)
admin.site.register(ProductWrapper)
admin.site.register(CustomerProductList)