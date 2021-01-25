from django.forms import ModelForm
from .models import Housemate_eats


class EetMeeForm(ModelForm):
    class Meta:
        model = Housemate_eats
        fields = ['eetmee']
        labels = {
            'eetmee': ''
        }