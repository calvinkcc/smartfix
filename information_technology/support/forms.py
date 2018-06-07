from django import forms
from support.models import Contact
from django.core import validators

class Contact_Form(forms.ModelForm):
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Contact
        fields = "__all__"
