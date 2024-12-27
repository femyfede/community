from django import forms
from .models import Payment


class PaymentForm(forms.Form):
    email = forms.EmailField()
    payment_method = forms.ChoiceField(
        choices=[ ('phone', 'Phone Number')],
        widget=forms.RadioSelect,
        label='Payment Method',
    )
