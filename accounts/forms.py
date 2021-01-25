from django import forms
from .models import Housemate_eats


class EetMeeForm(forms.ModelForm):
    class Meta:
        model = Housemate_eats
        fields = ['eetmee']
        labels = {
            'eetmee': ''
        }


class inschrijvenForm(forms.Form):
    ingeschreven = forms.BooleanField(label='')