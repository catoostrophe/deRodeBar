from django.contrib import admin
from .models import Housemate, Cook, Housemate_eats

admin.site.register(Housemate)
admin.site.register(Cook)
admin.site.register(Housemate_eats)
