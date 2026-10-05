from functools import wraps

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from django.contrib.auth.decorators import (
    login_required
)

from users.models import User

from .forms import AdminUserForm


def admin_required(view_func):

    @wraps(view_func)
    @login_required
    def wrapper(
        request,
        *args,
        **kwargs
    ):

        if request.user.role != 'admin':
            messages.error(
                request,
                "Admin access required."
            )

            return redirect(
                'user_home'
            )

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper


@admin_required
def admin_home(request):

    users = User.objects.all().order_by(
        '-id'
    )

    return render(
        request,
        'adminpanel/home.html',
        {
            'users': users
        }
    )


@admin_required
def add_user(request):

    if request.method == 'POST':
        form = AdminUserForm(
            request.POST
        )

        if form.is_valid():
            user = form.save(
                commit=False
            )

            password = form.cleaned_data.get(
                'password'
            )

            if password:
                user.set_password(
                    password
                )

            user.save()

            messages.success(
                request,
                "User added successfully."
            )

            return redirect(
                'admin_home'
            )

    else:
        form = AdminUserForm()

    return render(
        request,
        'adminpanel/add_user.html',
        {
            'form': form
        }
    )


@admin_required
def edit_user(
    request,
    user_id
):

    user = get_object_or_404(
        User,
        id=user_id
    )

    if request.method == 'POST':
        form = AdminUserForm(
            request.POST,
            instance=user
        )

        if form.is_valid():
            user = form.save(
                commit=False
            )

            password = form.cleaned_data.get(
                'password'
            )

            if password:
                user.set_password(
                    password
                )

            user.save()

            messages.success(
                request,
                "User updated successfully."
            )

            return redirect(
                'admin_home'
            )

    else:
        form = AdminUserForm(
            instance=user
        )

    return render(
        request,
        'adminpanel/edit_user.html',
        {
            'form': form,
            'user': user
        }
    )


@admin_required
def delete_user(
    request,
    user_id
):

    user = get_object_or_404(
        User,
        id=user_id
    )

    if user == request.user:
        messages.error(
            request,
            "You cannot delete your own admin account."
        )

        return redirect(
            'admin_home'
        )

    user.delete()

    messages.success(
        request,
        "User deleted successfully."
    )

    return redirect(
        'admin_home'
    )