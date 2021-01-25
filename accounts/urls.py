from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from .views import SignUpView, home_view, eetMee

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home_view, name='home'),
    path('eet/<date>', eetMee, name='eet')
]
