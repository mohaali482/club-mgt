from django.urls import path

from .views import (DivisionCreateView, DivisionDeleteView, DivisionDetailView,
                    DivisionListView, DivisionUpdateView)

urlpatterns = [
    path('register/', DivisionCreateView.as_view(), name="division-register"),
    path('list/', DivisionListView.as_view(), name="division-list"),
    path('<slug:id>/detail/', DivisionDetailView.as_view(), name="division-detail"),
    path('<slug:id>/delete/', DivisionDeleteView.as_view(), name="division-delete"),
    path('<slug:id>/edit/', DivisionUpdateView.as_view(), name="division-edit"),
]
