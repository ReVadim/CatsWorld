from django import forms

from .models import Cats


class RegisterCatForm(forms.ModelForm):
    """ Add new users pet """
    def __init__(self, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner

    def save(self, *args, **kwargs):
        self.instance.owner = self.owner
        return super(RegisterCatForm, self).save(*args, **kwargs)

    class Meta:
        model = Cats
        fields = ['name', 'birthday', 'color', 'temperament', 'description', 'photo']
