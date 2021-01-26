import datetime
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .models import Housemate, Cook, Housemate_eats
from .forms import EetMeeForm, inschrijvenForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home_view(request):
    user_objects = Housemate.objects.all()
    date = datetime.date(2021, 1, 25)
    form = EetMeeForm
    form_inschrijven = inschrijvenForm
    cook = Cook.objects.all()
    cook2 = Cook.objects.get(date=date)
    eetmee = Housemate_eats.objects.filter(cook_id=cook2.pk)
    names = []
    cookExists = False
    theCook = None

    for housemate in eetmee:
        names.append(housemate.name)

    if Cook.objects.filter(date=date).exists():
        cookExists = True
        theCook = Cook.objects.get(date=date).kok


    context = {
        'user_objects': user_objects,
        'date': date,
        'form': form,
        'form_inschrijven': form_inschrijven,
        'cook': cook,
        'eetmee': eetmee,
        'names': names,
        'cookExists': cookExists,
        'theCook': theCook
    }

    return render(request, 'home.html', context)


def eetMee(request, date, name):
    form = EetMeeForm(request.POST)

    if form.is_valid():
        cook = Cook.objects.get(date=date)

        if Housemate_eats.objects.filter(cook_id=cook.pk, name=name).exists():
            eat = Housemate_eats.objects.get(cook_id=cook.pk, name=name)
            eat.eetmee = form.cleaned_data['eetmee']
            eat.save()
        else:
            newEat = Housemate_eats(name=name, eetmee=form.cleaned_data['eetmee'], cook=cook)
            newEat.save()

    return redirect('home')


def inschrijven(request, date, name):
    form_inschrijven = inschrijvenForm(request.POST)

    if form_inschrijven.is_valid():
        cook = Cook(date=date, kok=name)
        cook.save()

    return redirect('home')
