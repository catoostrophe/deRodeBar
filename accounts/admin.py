from django.contrib import admin
from .models import Housemate, Cook, HousemateCook

admin.site.register(Housemate)
admin.site.register(Cook)
admin.site.register(HousemateCook)
