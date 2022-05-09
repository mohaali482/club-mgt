from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/',
        views.activate, name='activate'),
]