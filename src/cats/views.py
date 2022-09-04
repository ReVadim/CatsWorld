from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from src.account.models import CatsOwner
from src.cats.forms import RegisterCatForm
from src.cats.models import Cats


@login_required()
def detail(request):
    """ Information about users pets """
    cats = Cats.objects.filter(owner=request.user)
    context = {'cats': cats}
    return render(request, 'cats/pets.html', context)


class RegisterPetView(CreateView):
    """ New user registration
    """
    model = Cats
    template_name = 'cats/register_pet.html'
    form_class = RegisterCatForm
    success_url = reverse_lazy('src.cats:detail')

    def get_form_kwargs(self):
        kwargs = super(RegisterPetView, self).get_form_kwargs()
        kwargs.update({'owner': self.request.user if self.request.user.is_authenticated else None, })
        return kwargs
