from django import forms
from .models import UsersPromocode

class NewPromoForm(forms.ModelForm):
    class Meta:
        model = UsersPromocode
        fields = [
            'new_promo',
        ]