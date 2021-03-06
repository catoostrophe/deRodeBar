from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from .views import home_view, eetMee, inschrijven

urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('', home_view, name='home'),
    path('eet/<date>/<name>', eetMee, name='eet'),
    path('inschrijven/<date>/<name>', inschrijven, name='inschrijven')
]
