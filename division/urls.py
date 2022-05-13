from django.urls import path

from .views import (DivisionCreateView, DivisionDeleteView, DivisionDetailView,
                    DivisionListView, DivisionUpdateView, DivisionHeadCreateView,
                    DivisionHeadDeleteView, DivisionHeadListView)

urlpatterns = [
    path('register/', DivisionCreateView.as_view(), name="division-register"),
    path('', DivisionListView.as_view(), name="division-list"),
    path('<slug:id>/detail/', DivisionDetailView.as_view(), name="division-detail"),
    path('<slug:id>/delete/', DivisionDeleteView.as_view(), name="division-delete"),
    path('<slug:id>/edit/', DivisionUpdateView.as_view(), name="division-edit"),
    path('head/register/', DivisionHeadCreateView.as_view(), name="division-head-register"),
    path('head/', DivisionHeadListView.as_view(), name="division-head-delete"),
    path('head/<slug:id>/delete/', DivisionHeadDeleteView.as_view(), name="division-head-delete"),
]
