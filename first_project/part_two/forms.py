from django import forms
from part_two.models import Users

class user_form(forms.ModelForm):   
    class Meta:
        model = Users
        fields = "__all__"
        