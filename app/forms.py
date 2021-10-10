
from .models import order
from django.forms import  ModelForm, TextInput

class orderForm(ModelForm):
    class Meta:
        model = order
        fields =['name', 'email', 'phone', 'message']
        widgets = {
            'name':TextInput(attrs={
                'class':'form-group',
                 'placeholder': 'Name'
            }),
            'email':TextInput(attrs={
                'class':'form-group',
                'placeholder': 'Email'

            }),
            'phone':TextInput(attrs={
                'class':'form-group',
                'placeholder': '998XXXXXXXXX'
            }),
            'message':TextInput(attrs={
                'class':'form-group',
                'placeholder': 'Message'
            }),
            
        }
        