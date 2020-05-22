from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"      # This is for all the fields of the model

        # For creating for specific fields Use fields = ["customer", "product"]

        
