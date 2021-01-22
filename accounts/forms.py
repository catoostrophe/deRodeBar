from django.forms import ModelForm
from .models import HousemateCook


class EetMeeForm(ModelForm):
    class Meta:
        model = HousemateCook
        fields = ['eetMee']
        labels = {
            'eetMee': ''
        }