from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('event/<str:name>', index),
    path('list/' , list_event),
    path('affiche/', ListEvents.as_view(), name="Affiche"),
    path('add/', AddEvent.as_view(), name="add"),
    path('delete/<int:pk>', views.deleteEvent, name="delete"),
    path('update/<int:pk>', views.updateEvent, name="update")


]