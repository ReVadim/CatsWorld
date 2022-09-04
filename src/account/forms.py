from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .apps import user_registered
from .models import CatsOwner


class RegisterUserForm(forms.ModelForm):
    """ Form for new user registration
    """
    email = forms.EmailField(required=True, label=_('email address'))
    password = forms.CharField(
        label=_('password'), widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )
    confirm_password = forms.CharField(
        label=_('password again'), widget=forms.PasswordInput, help_text=_('re-enter the password')
    )

    def clean_password(self):

        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)

        return password

    def clean(self):

        super().clean()
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            errors = {'confirm_password': ValidationError(_("passwords don't match"), code='password_mismatch')}

            raise ValidationError(errors)

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registered.send(RegisterUserForm, instance=user)

        return user

    class Meta:
        model = CatsOwner
        fields = [
            'username', 'avatar', 'email', 'password', 'confirm_password', 'country', 'city', 'about', 'send_message'
        ]


class ChangeUserInfoForm(forms.ModelForm):
    """ Change user information form
    """
    email = forms.EmailField(required=True, label=_('email address'))

    class Meta:
        model = CatsOwner
        fields = ['username', 'country', 'city', 'email', 'send_message', 'avatar', 'about']
