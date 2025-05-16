from django.db import models
from seller.models import Seller


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    listing_date = models.DateField()
    nr_rooms = models.IntegerField()
    nr_bedrooms = models.IntegerField()
    nr_bathrooms = models.IntegerField()
    nr_square_meters = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=255)
    price = models.FloatField()
    on_sale = models.BooleanField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class Property_image(models.Model):
    image = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


