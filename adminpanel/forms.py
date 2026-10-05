import re
from django import forms
from users.models import User


class AdminUserForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = [
            'name',
            'mobile',
            'role',
            'password'
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

        existing_user = User.objects.filter(
            mobile=mobile
        ).exclude(
            id=self.instance.id
        )

        if existing_user.exists():
            raise forms.ValidationError(
                "Mobile number already registered."
            )

        return mobile

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if password:
            if len(password) < 6:
                raise forms.ValidationError(
                    "Password must contain at least 6 characters."
                )

            if not re.search(
                r'[A-Z]',
                password
            ):
                raise forms.ValidationError(
                    "Password needs an uppercase letter."
                )

            if not re.search(
                r'[a-z]',
                password
            ):
                raise forms.ValidationError(
                    "Password needs a lowercase letter."
                )

            if not re.search(
                r'[0-9]',
                password
            ):
                raise forms.ValidationError(
                    "Password needs a number."
                )

            if not re.search(
                r'[^A-Za-z0-9]',
                password
            ):
                raise forms.ValidationError(
                    "Password needs a special character."
                )

        return password