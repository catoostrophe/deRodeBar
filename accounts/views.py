import datetime
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Housemate, Cook
from .forms import EetMeeForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home_view(request):
    user_objects = Housemate.objects.all()
    date = datetime.datetime.now().date()
    form = EetMeeForm
    cook = Cook.objects.all()

    context = {
        'user_objects': user_objects,
        'date': date,
        'form': form,
        'cook': cook
    }

    return render(request, 'home.html', context)
