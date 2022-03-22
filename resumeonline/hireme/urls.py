from django.urls import path
from . import views

urlpatterns = [
    path('hireme', views.hireme, name='hireme'),
]
