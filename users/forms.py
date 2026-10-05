import re
from django import forms
from .models import User


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = [
            'name',
            'mobile',
            'password',
            'confirm_password'
        ]

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']

        if not mobile.isdigit():
            raise forms.ValidationError(
                "Mobile number must contain only numbers."
            )

        if len(mobile) != 10:
            raise forms.ValidationError(
                "Mobile number must contain 10 digits."
            )

        if User.objects.filter(
            mobile=mobile
        ).exists():
            raise forms.ValidationError(
                "Mobile number already registered."
            )

        return mobile

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 6:
            raise forms.ValidationError(
                "Password must contain at least 6 characters."
            )

        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError(
                "Password must contain an uppercase letter."
            )

        if not re.search(r'[a-z]', password):
            raise forms.ValidationError(
                "Password must contain a lowercase letter."
            )

        if not re.search(r'[0-9]', password):
            raise forms.ValidationError(
                "Password must contain a number."
            )

        if not re.search(
            r'[^A-Za-z0-9]',
            password
        ):
            raise forms.ValidationError(
                "Password must contain a special character."
            )

        return password

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get(
            'password'
        )

        confirm_password = cleaned_data.get(
            'confirm_password'
        )

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data


class LoginForm(forms.Form):

    mobile = forms.CharField(
        max_length=15
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'name',
            'mobile'
        ]

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']

        if not mobile.isdigit():
            raise forms.ValidationError(
                "Mobile number must contain only numbers."
            )

        if len(mobile) != 10:
            raise forms.ValidationError(
                "Mobile number must contain 10 digits."
            )

        if User.objects.filter(
            mobile=mobile
        ).exclude(
            id=self.instance.id
        ).exists():
            raise forms.ValidationError(
                "Mobile number already registered."
            )

        return mobile