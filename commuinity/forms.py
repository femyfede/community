from django import forms
from .models import Payment


class PaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=15, required=True, label='Phone Number')
    payment_method = forms.ChoiceField(
        choices=[('card', 'Credit/Debit Card'), ('phone', 'Phone Number')],
        widget=forms.RadioSelect,
        label='Payment Method',
    )
