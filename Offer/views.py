from django.shortcuts import render
from .models import PurchaseOffer
# Create your views here.

def offer_list(request):
    offers = PurchaseOffer.objects.select_related('property', 'property__seller').all()
    return render(request, "offer/offer_list.html", {
        'offers': offers
    })


