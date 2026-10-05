from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.admin_home,
        name='admin_home'
    ),
    path(
        'add-user/',
        views.add_user,
        name='add_user'
    ),
    path(
        'edit-user/<int:user_id>/',
        views.edit_user,
        name='edit_user'
    ),
    path(
        'delete-user/<int:user_id>/',
        views.delete_user,
        name='delete_user'
    ),
]