from django.urls import path

from .views import (SubDivisionCreateView, SubDivisionDeleteView,
                    SubDivisionDetailView, SubDivisionListView,
                    SubDivisionUpdateView)

urlpatterns = [
    path('', SubDivisionListView.as_view(), name="sub-division-list"),
    path('register/', SubDivisionCreateView.as_view(),
         name="sub-division-register"),
    path('<slug:id>/delete/', SubDivisionDeleteView.as_view(),
         name="sub-division-delete"),
    path('<slug:id>/detail/', SubDivisionDetailView.as_view(),
         name="sub-division-detail"),
    path('<slug:id>/update/', SubDivisionUpdateView.as_view(),
         name="sub-division-update"),
]
