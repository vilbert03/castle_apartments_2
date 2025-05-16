from django.db import models
from Property.models import Property
from django.contrib.auth.models import User



class PurchaseOffer(models.Model):
    status_choice = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Contigent', 'Contigent'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    offer_price = models.FloatField()
    date_submitted = models.DateField(auto_now_add=True)
    date_expired = models.DateField()
    status = models.CharField(max_length=20, choices=status_choice, default='Pending')

    def __str__(self):
        return f' the offer on {self.property.name} - {self.date_expired} ISK'


class FinalizedPurchase(models.Model):
    offer = models.OneToOneField(PurchaseOffer, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    payment_method = models.CharField(max_length=20, choices=[
        ("credit_card", "Credit Card"),
        ("bank_transfer", "Bank Transfer"),
        ("mortgage", "Mortgage")
    ])

    cardholder_name = models.CharField(max_length=255, blank=True, null=True)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    expiry_date = models.CharField(max_length=7, blank=True, null=True)
    cvc = models.CharField(max_length=5, blank=True, null=True)

    bank_account = models.CharField(max_length=50, blank=True, null=True)

    mortgage_provider = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Finalization for Offer #{self.offer.id}"

