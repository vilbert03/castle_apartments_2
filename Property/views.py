from django.shortcuts import render, get_object_or_404
from .models import Property
from django.contrib import messages


def index(request):
    properties = Property.objects.select_related('seller').all()
    return render(request, "property/properties.html", {
        "properties": properties
    })

def get_property_by_id(request, id):
    property_obj = get_object_or_404(Property.objects.select_related('seller'), id=id)
    return render(request, 'property/properties_detail_page.html', {
        "property": property_obj
    })


def make_an_offer(request, id):
    prop = next((x for x in properties if x['id'] == id), None)
    if not prop:
        return HttpResponse("Property not found", status=404)

    if request.method == "POST":
        offer_price = request.POST.get('offer_price')
        expiration_date = request.POST.get('expiration_date')

        messages.success(request, 'Your offer has been submitted successfully!')

        return redirect('property:property_by_id', id=id)

    return render(request, 'property/make_an_offer.html', {'property': prop})

