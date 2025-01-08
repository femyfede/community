from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment  # Link the form to the Payment model
        fields = ['transaction_id', 'amount']  # Include only the fields needed for payment


    transaction_id = forms.CharField(max_length=100)
    email = forms.EmailField()
    payment_method = forms.ChoiceField(
        choices=[ ('phone', 'Phone Number')],
        widget=forms.RadioSelect,
        label='Payment Method',
    )
