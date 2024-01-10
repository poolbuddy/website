from django.db import models
from django.contrib.postgres.fields import ArrayField


def default_image():
    return ['default_image.jpg']


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(default="default")
    picture_1 = models.ImageField(null=True, blank=True)
    picture_2 = models.ImageField(null=True, blank=True)
    picture_3 = models.ImageField(null=True, blank=True)
    picture_4 = models.ImageField(null=True, blank=True)
    is_chemical = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.id}"

class ProductWrapper(models.Model):
    customer_email = models.EmailField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)
    ordered = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    date_delivered = models.DateField(null=True, blank=True)
    date_purchased = models.DateField(null=True, blank=True)
    requested_speed = models.CharField()
    payment_method = models.CharField()
    delivery_type = models.CharField()
    returned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id} - {self.customer_email} - {self.product}"

class CustomerProductList(models.Model):
    product_list = models.ManyToManyField(ProductWrapper, blank=True)
    def __str__(self):
        return f"id = {self.id}" 