from django.contrib.auth.views import LoginView
from django.core.signing import BadSignature
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from src.account.forms import RegisterUserForm
from src.account.models import CatsUser
from src.account.services import signer


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
    user = get_object_or_404(CatsUser, username=username)
    if user.is_activated:
        template = 'account/user_is_activated.html'
    else:
        template = 'account/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


class RegisterUserView(CreateView):
    """ New user registration
    """
    model = CatsUser
    template_name = 'account/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('src.account:register_done')


class RegisterDoneView(TemplateView):
    """ Displays a message about successful registration
    """
    template_name = 'account/register_done.html'


class CatsUserLoginView(LoginView):
    """ Standard authentication model
    """
    template_name = 'account/login.html'

