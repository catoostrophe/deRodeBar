from django.forms import ModelForm
from .models import HousemateEats


class EetMeeForm(ModelForm):
    class Meta:
        model = HousemateEats
        fields = ['eetMee']
        labels = {
            'eetMee': ''
        }