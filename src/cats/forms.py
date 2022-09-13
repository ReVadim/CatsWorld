from django import forms
from .models import Cats


class RegisterCatForm(forms.ModelForm):
    """ Add new users pet
    """
    birthday = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}))

    def __init__(self, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner

    def save(self, *args, **kwargs):
        self.instance.owner = self.owner
        return super(RegisterCatForm, self).save(*args, **kwargs)

    class Meta:
        model = Cats
        fields = ['name', 'birthday', 'color', 'temperament', 'description', 'photo']


class ChangePetInfoForm(forms.ModelForm):
    """ Change pet info
    """
    birthday = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}))

    class Meta:
        model = Cats
        fields = ['name', 'birthday', 'color', 'temperament', 'description', 'photo']
