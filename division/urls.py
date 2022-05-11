from django.urls import path

from .views import DivisionCreateView, DivisionListView, DivisionDetailView

urlpatterns = [
    path('register/', DivisionCreateView.as_view(), name="division-register"),
    path('list/', DivisionListView.as_view(), name="division-list"),
    path('<slug:id>/detail/', DivisionDetailView.as_view(), name="division-detail"),
]
