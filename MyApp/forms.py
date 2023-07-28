
from MyApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


class ProductSearchForm(forms.ModelForm):
	
	ProductName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'ProductName', 'placeholder' : 'Enter Product Name'})

	)
	


	class Meta:
		model = Products
		fields =['ProductName']
class ContactMeForm(forms.ModelForm):
	

	class Meta:
		model = ContactMe
		fields =['email','phone','place','message']



PAYMENT_CHOICES = (
    ('S', 'M-PESA'),
    ('P', 'TIGO PESA'),
    ('H', 'HALO PESA'),
    ('A', 'AIRTEL MONEY'),
)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Promo code",
        'aria-label ': "Recipient's username",
        'aria-describedby': "basic-addon2"
    }), max_length=50)

class AddressForm(forms.Form):
    street_address = forms.CharField()
    apartment_address = forms.CharField()
    country = CountryField(blank_label="Select country").formfield(widget=CountrySelectWidget(attrs={
        "class": "custom-select d-block w-100"
    }))
    zip = forms.CharField(required=False)
    save_info = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)