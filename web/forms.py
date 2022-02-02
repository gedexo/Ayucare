from django import forms
from .models import Contact,Subscribe
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,TimeInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name',}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone',}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email',}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
              
            }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Name',}),
            
            }