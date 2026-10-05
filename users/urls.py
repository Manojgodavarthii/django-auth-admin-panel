from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.login_view,
        name='login'
    ),
    path(
        'login/',
        views.login_view,
        name='login'
    ),
    path(
        'register/',
        views.register,
        name='register'
    ),
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
    path(
        'user/home/',
        views.user_home,
        name='user_home'
    ),
    path(
        'user/edit/',
        views.edit_profile,
        name='edit_profile'
    ),
]