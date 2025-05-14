from django.shortcuts import render, get_object_or_404, redirect
from Property.models import Property
from django.contrib import messages
from django.http import JsonResponse
from Offer.models import PurchaseOffer
from datetime import datetime


def index(request):
    if 'search_filter' in request.GET:
        return JsonResponse({
            'data': [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
                'description': x.description,
                'type': x.type,
                'image': x.property_image_set.first().image if x.property_image_set.exists() else None,
            }for x in Property.objects.filter(name__icontains=request.GET['search_filter']).order_by('name')]
        })

    properties = Property.objects.select_related('seller').all()
    return render(request, "property/properties.html", {
        "properties": properties
    })

def get_property_by_id(request, id):
    property_obj = get_object_or_404(Property.objects.select_related('seller'), id=id)
    return render(request, 'property/properties_detail_page.html', {
        "property": property_obj
    })


#def make_an_offer(request, id):
#    prop = get_object_or_404(Property, id=id)
#
#    if request.method == "POST":
#        offer_price = request.POST.get('offer_price')
#        expiration_date = request.POST.get('expiration_date')
#
#        if offer_price and expiration_date:
#            try:
#                expiration_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d').date()
#
#                PurchaseOffer.objects.create(
#                    property=prop,
#                    offer_price=float(offer_price),
#                    date_expired=expiration_date_obj
#                )
#
#                messages.success(request, "Your offer has been submitted successfully!")
#                return redirect('property:property_by_id', id=id)
#
#            except ValueError:
#                messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
#        else:
#            messages.error(request, "Please fill in all fields.")
#
#    return render(request, 'property/make_an_offer.html', {'property': prop})

