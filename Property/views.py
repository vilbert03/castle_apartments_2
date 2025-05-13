from django.shortcuts import render, get_object_or_404
from .models import Property

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