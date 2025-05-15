from django.shortcuts import render, get_object_or_404, redirect
from Property.models import Property
from django.contrib import messages
from django.http import JsonResponse
from Offer.models import PurchaseOffer
from datetime import datetime


def index(request):
    queryset = Property.objects.select_related('seller').all()

    if search := request.GET.get("search_filter"):
        queryset = queryset.filter(name__icontains=search)

    if postal := request.GET.get("postal_code"):
        queryset = queryset.filter(postal_code=postal)

    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    if min_price:
        queryset = queryset.filter(price__gte=min_price)
    if max_price:
        queryset = queryset.filter(price__lte=max_price)

    if ptype := request.GET.get("type"):
        queryset = queryset.filter(type__iexact=ptype)

    if order_by := request.GET.get("order_by"):
        if order_by in ["name", "price"]:
            queryset = queryset.order_by(order_by)

    return render(request, "property/properties.html", {
        "properties": queryset
    })

def get_property_by_id(request, id):
    property_obj = get_object_or_404(Property.objects.select_related('seller'), id=id)
    offer = PurchaseOffer.objects.filter(property=property_obj).first()
    return render(request, 'property/properties_detail_page.html', {
        "property": property_obj,
        "offer": offer,
    })

