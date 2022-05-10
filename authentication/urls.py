from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',
         auth_views.LoginView.as_view(
             template_name="authentication/login.html"),
         name="login"),
    path('signup/', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.UserUpdateView.as_view(), name='update-profile'),
    path('detail/<slug:id>/', views.UserDetailView.as_view(), name='detail-profile'),
]
