from django.shortcuts import render, get_object_or_404
from .models import Seller

def index(request):
    sellers = Seller.objects.all()
    return render(request, "seller/sellers.html", {
        "sellers": sellers
    })

def get_seller_by_id(request, id):
    seller = get_object_or_404(Seller, id=id)
    properties = seller.property_set.all()  # related properties
    return render(request, "seller/seller_detail.html", {
        "seller": seller,
        "properties": properties
    })
