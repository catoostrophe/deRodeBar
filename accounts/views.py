import datetime
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .models import Housemate, Cook, Housemate_eats
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
    cook2 = Cook.objects.get(date=date)
    eetmee = Housemate_eats.objects.filter(cook_id=cook2.pk)
    names = []

    for housemate in eetmee:
        names.append(housemate.name)

    context = {
        'user_objects': user_objects,
        'date': date,
        'form': form,
        'cook': cook,
        'eetmee': eetmee,
        'names': names
    }

    return render(request, 'home.html', context)


def eetMee(request, date, name):
    form = EetMeeForm(request.POST)

    if form.is_valid():
        cook = Cook.objects.get(date=date)

        if Housemate_eats.objects.filter(cook_id=cook.pk, name=name).exists():
            eat = Housemate_eats.objects.get(cook_id=cook.pk, name=name)
            eat.eetmee = request.POST['eetmee']
            eat.save()
        else:
            newEat = Housemate_eats(name=name, eetmee=request.POST['eetmee'], cook=cook)
            newEat.save()

    return redirect('home')


def showEetmee(request, date, name):
    cook = Cook.objects.get(date=date)
    eat = Housemate_eats.objects.get(cook_id=cook.pk, name=name)

    context = {
        'eetmee': eat
    }

    redirect('home')
    return render(request, 'home.html', context)
