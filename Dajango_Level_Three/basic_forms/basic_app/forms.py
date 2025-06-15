from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField(max_length = 255)
    email = forms.EmailField(max_length= 255)
    verify_email = forms.EmailField(label = "enter the email once again : ")
    text = forms.CharField( widget = forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email')
        vmail = all_clean_data.get('verify_email')
        
        if email != vmail:
            raise forms.ValidationError("emails must in same...please correct...")     