from django import forms # type: ignore
from .models import Farmer, Order

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'email', 'phone']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['fertilizer_name', 'quantity', 'address', 'delivery_date', 'payment_method']  # Remove 'farmer' and 'fertilizer'

class FarmerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'email', 'phone']  # Ensure fields match your model

