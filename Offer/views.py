from django.shortcuts import render, get_object_or_404, redirect
from .models import PurchaseOffer
from .forms import PurchaseOfferForm
from Property.models import Property
from django.contrib import messages
# Create your views here.

def offer_list(request):
    offers = PurchaseOffer.objects.select_related('property', 'property__seller').all()
    return render(request, "offer/offer_list.html", {
        'offers': offers
    })


def make_an_offer(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        form = PurchaseOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.property = property_obj
            offer.save()
            messages.success(request, "Your offer has been submitted.")
            return redirect('property:property_by_id', id=property_id)
    else:
        form = PurchaseOfferForm()

    return render(request, 'offer/make_an_offer.html', {
        'form': form,
        'property': property_obj
    })

