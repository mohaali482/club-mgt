from django.shortcuts import render
from django.urls import path

from .views import EventCreateView, EventListView, EventUpdateView

urlpatterns = [
    path('', EventListView.as_view(), name="event-home"),
    path('create/', EventCreateView.as_view(), name="event-create"),
    path('<slug:pk>/update/', EventUpdateView.as_view(), name="event-update")
]
