from django.shortcuts import render, get_object_or_404, redirect
from .models import PurchaseOffer, FinalizedPurchase
from .forms import *
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

def finalize_step1(request, offer_id):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            request.session['finalize_data'] = form.cleaned_data
            return redirect('Offer:finalize_step2', offer_id=offer_id)
    else:
        form = ContactInfoForm()

    return render(request, 'offer/finalize_step1.html', {
        'form': form,
        'offer_id': offer_id
    })

def finalize_step2(request, offer_id):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Merge contact info and payment info into one session dict
            contact_data = request.session.get('finalize_data', {})
            contact_data.update(form.cleaned_data)
            request.session['finalize_data'] = contact_data

            return redirect('Offer:finalize_review', offer_id=offer_id)
    else:
        form = PaymentForm()

    return render(request, 'offer/finalize_step2.html', {
        'form': form,
        'offer_id': offer_id
    })


def finalize_review(request, offer_id):
    offer = get_object_or_404(PurchaseOffer, id=offer_id)

    data = request.session.get('finalize_data')
    if not data:
        messages.error(request, "Missing data. Please complete previous steps.")
        return redirect('Offer:finalize_step1', offer_id=offer_id)

    if request.method == 'POST':
        # Save to DB
        FinalizedPurchase.objects.create(
            offer=offer,
            full_name=data['full_name'],
            national_id=data['national_id'],
            street=data['street'],
            city=data['city'],
            postal_code=data['postal_code'],
            country=data['country'],
            payment_method=data['payment_method'],
            cardholder_name=data.get('cardholder_name'),
            card_number=data.get('card_number'),
            expiry_date=data.get('expiry_date'),
            cvc=data.get('cvc'),
            bank_account=data.get('bank_account'),
            mortgage_provider=data.get('mortgage_provider'),
        )
        messages.success(request, "Purchase offer finalized successfully!")
        # Clear session
        request.session.pop('finalize_data', None)
        return redirect('Offer:finalize_success')

    return render(request, 'offer/finalize_review.html', {
        'data': data,
        'offer': offer
    })


def finalize_success(request):
    return render(request, 'offer/finalize_success.html')
