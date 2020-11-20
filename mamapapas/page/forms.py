from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Email'}), label='', max_length=120)
    name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Имя'}), label='', max_length=120)
    phone = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Телефон'}), label='', max_length=120)
