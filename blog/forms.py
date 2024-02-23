from django import forms
from.models import Kansultatsiya





class KansultatsiyaForms(forms.ModelForm):


    class Meta:
        model = Kansultatsiya
        fields = "__all__"




























