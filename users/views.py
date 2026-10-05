from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib import messages

from django.contrib.auth.decorators import (
    login_required
)

from .forms import (
    RegisterForm,
    LoginForm,
    UserUpdateForm
)


def register(request):

    if request.user.is_authenticated:
        if request.user.role == 'admin':
            return redirect(
                'admin_home'
            )
        return redirect(
            'user_home'
        )

    if request.method == 'POST':
        form = RegisterForm(
            request.POST
        )

        if form.is_valid():
            user = form.save(
                commit=False
            )

            user.set_password(
                form.cleaned_data[
                    'password'
                ]
            )

            user.role = 'user'
            user.save()

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect(
                'login'
            )

    else:
        form = RegisterForm()

    return render(
        request,
        'users/register.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.user.is_authenticated:
        if request.user.role == 'admin':
            return redirect(
                'admin_home'
            )
        return redirect(
            'user_home'
        )

    if request.method == 'POST':
        form = LoginForm(
            request.POST
        )

        if form.is_valid():
            mobile = form.cleaned_data[
                'mobile'
            ]

            password = form.cleaned_data[
                'password'
            ]

            user = authenticate(
                request,
                mobile=mobile,
                password=password
            )

            if user is not None:
                login(
                    request,
                    user
                )

                if user.role == 'admin':
                    return redirect(
                        'admin_home'
                    )

                return redirect(
                    'user_home'
                )

            messages.error(
                request,
                "Invalid mobile number or password."
            )

    else:
        form = LoginForm()

    return render(
        request,
        'users/login.html',
        {
            'form': form
        }
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect(
        'login'
    )


@login_required
def user_home(request):

    if request.user.role == 'admin':
        return redirect(
            'admin_home'
        )

    return render(
        request,
        'users/home.html'
    )


@login_required
def edit_profile(request):

    if request.user.role == 'admin':
        return redirect(
            'admin_home'
        )

    if request.method == 'POST':
        form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect(
                'user_home'
            )

    else:
        form = UserUpdateForm(
            instance=request.user
        )

    return render(
        request,
        'users/edit_profile.html',
        {
            'form': form
        }
    )