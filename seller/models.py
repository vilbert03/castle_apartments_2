from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=4096)
    logo = models.CharField(max_length=4096)
    cover_image = models.CharField(max_length=4096)

    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)

    def is_agency(self):
        return self.type.lower() == "agency" or "Real Estate Agent"

    def __str__(self):
        return self.name
