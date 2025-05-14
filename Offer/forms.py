from django import forms
from .models import PurchaseOffer


class PurchaseOfferForm(forms.ModelForm):
    class Meta:
        model = PurchaseOffer
        fields = ['offer_price', 'date_expired']
        widgets = {
            'date_expired': forms.DateInput(attrs={'type': 'date'}),
        }


