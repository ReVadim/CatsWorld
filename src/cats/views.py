from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from src.cats.forms import RegisterCatForm, ChangePetInfoForm, AddPhotoToAlbumForm
from src.cats.models import Cats, PetPhotoAlbum


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


def pet_detail(request, pk):
    """ Full information about pet
    """
    pet = Cats.objects.filter(pk=pk)
    images = PetPhotoAlbum.objects.filter(pet_id=pk)
    context = {'pet': pet, 'images': images}
    return render(request, 'cats/pet_detail.html', context)


class ChangePetDetailView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Change information about pet
    """
    model = Cats
    template_name = 'cats/change_pet_info.html'
    form_class = ChangePetInfoForm
    success_url = reverse_lazy('src.cats:detail')
    success_message = 'Данные успешно изменены'

    def setup(self, request, *args, **kwargs):
        self.cats_id = kwargs['pk']
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.cats_id)


class AddPhotoToAlbumView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ Add new photo to album
    """
    model = PetPhotoAlbum
    template_name = 'cats/add_photo_to_album.html'
    form_class = AddPhotoToAlbumForm
    success_url = reverse_lazy('src.cats:detail')
    success_message = 'Фотография успешно добавлена'

    def setup(self, request, *args, **kwargs):
        self.cats_id = kwargs['pet_id']
        return super().setup(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(AddPhotoToAlbumView, self).get_form_kwargs()
        kwargs['pet_id'] = self.cats_id
        return kwargs