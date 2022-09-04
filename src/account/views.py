from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.signing import BadSignature
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView

from src.account.forms import RegisterUserForm, ChangeUserInfoForm
from src.account.models import CatsOwner
from src.base.services import signer


def index(request):
    """ Main page
    """
    return render(request, 'account/index.html')


def user_activate(request, sign):
    """ User activation
    """
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'account/bad_signature.html')
    user = get_object_or_404(CatsOwner, username=username)
    if user.is_activated:
        template = 'account/user_is_activated.html'
    else:
        template = 'account/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


@login_required()
def profile(request):
    """ User profile page
    """
    return render(request, 'account/profile.html')


class RegisterUserView(CreateView):
    """ New user registration
    """
    model = CatsOwner
    template_name = 'account/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('src.account:register_done')


class RegisterDoneView(TemplateView):
    """ Displays a message about successful registration
    """
    template_name = 'account/register_done.html'


class CatsOwnerLoginView(LoginView):
    """ Standard authentication model
    """
    template_name = 'account/login.html'


class AccountLogoutView(LoginRequiredMixin, LogoutView):
    """ Standard logout view
    """
    template_name = 'account/logout.html'


class AccountPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    """ Change user password class
    """
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('src.account:profile')
    success_message = _('Password changed')


class DeleteUserView(LoginRequiredMixin, DeleteView):
    """ Delete User View
    """
    model = CatsOwner
    template_name = 'account/delete_user.html'
    success_url = reverse_lazy('src.account:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, _('User deleted'))
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Class for change user information
    """
    model = CatsOwner
    template_name = 'account/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('src.account:profile')
    success_message = _('User information changed')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

