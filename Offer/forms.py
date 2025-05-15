from django import forms
from .models import PurchaseOffer


class PurchaseOfferForm(forms.ModelForm):
    class Meta:
        model = PurchaseOffer
        fields = ['offer_price', 'date_expired']
        widgets = {
            'date_expired': forms.DateInput(attrs={'type': 'date'}),
        }

class ContactInfoForm(forms.Form):
    full_name = forms.CharField(label="Full Name")
    national_id = forms.CharField(label="National ID (Kennitala)")
    street = forms.CharField(label="Street Address")
    city = forms.CharField()
    postal_code = forms.CharField(label="Postal Code")
    country = forms.ChoiceField(choices=[
        ('IS', 'Iceland'),
        ('NO', 'Norway'),
        ('SE', 'Sweden'),
        ('DK', 'Denmark'),
        ('FI', 'Finland'),
    ])

class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=[
            ('credit_card', 'Credit Card'),
            ('bank_transfer', 'Bank Transfer'),
            ('mortgage', 'Mortgage')
        ],
        widget=forms.RadioSelect
    )

    # Credit card fields
    cardholder_name = forms.CharField(required=False)
    card_number = forms.CharField(required=False)
    expiry_date = forms.CharField(required=False)
    cvc = forms.CharField(required=False)

    # Bank transfer field
    bank_account = forms.CharField(required=False)

    # Mortgage field
    mortgage_provider = forms.CharField(required=False)
