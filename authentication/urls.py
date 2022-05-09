from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="authentication/login.html"), name="login" ),
    path('signup/', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/',
        views.activate, name='activate'),
]