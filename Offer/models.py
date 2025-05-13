from django.db import models
from Property.models import Property
# Create your models here.



class PurchaseOffer(models.Model):
    status_choice = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Contigent', 'Contigent'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    offer_price = models.FloatField()
    date_submitted = models.DateField(auto_now_add=True)
    date_expired = models.DateField()
    status = models.CharField(max_length=20, choices=status_choice, default='Pending')

    def __str__(self):
        return f' the offer on {self.property.name} - {self.date_expired} ISK'

