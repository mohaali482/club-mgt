from django.shortcuts import render
from django.urls import path

from .views import EventCreateView, EventDeleteView, EventDetailView, EventListView, EventUpdateView

urlpatterns = [
    path('', EventListView.as_view(), name="event-home"),
    path('create/', EventCreateView.as_view(), name="event-create"),
    path('<slug:id>/edit/', EventUpdateView.as_view(), name="event-edit"),
    path('<slug:id>/delete/', EventDeleteView.as_view(), name="event-delete"),
    path('<slug:id>/detail/', EventDetailView.as_view(), name="event-detail"),
]
