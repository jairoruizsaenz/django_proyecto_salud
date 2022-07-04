from django.urls import path
from .views import *
# from django.views.generic import TemplateView

app_name = 'baseApp'
urlpatterns = [
    path('inicio/', home, name='home'),
]