from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.account.models import CatsOwner
from ..base.services import get_path_upload_photo, validate_size_image, set_path_to_upload


def upload_into_album(instance, file):
    """ """
    owner_id = instance.pet.owner.id
    pet_id = instance.pet.id
    pet_name = instance.pet.name
    return set_path_to_upload(owner_id, pet_id, pet_name, file)


class Cats(models.Model):
    """ Main model include all information about cats
    """
    owner = models.ForeignKey(CatsOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name=_("name"))
    birthday = models.DateField()
    color = models.CharField(max_length=150, verbose_name=_("color"))
    temperament = models.CharField(max_length=35, blank=True, null=True, verbose_name=_("temperament"))
    description = models.CharField(max_length=300, blank=True, null=True, verbose_name=_("description"))
    photo = models.ImageField(
        upload_to=get_path_upload_photo,
        blank=True,
        null=True,
        verbose_name=_("avatar"),
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image]
    )

    def __str__(self):
        return f"{self.temperament} {self.name}"

    class Meta:
        verbose_name = _('pet')
        verbose_name_plural = _('pets')
        ordering = ['-birthday']
        db_table = 'pets'
        constraints = (
            models.UniqueConstraint(fields=('color', 'name', 'owner'),
                                    name='%(app_label)s_%(class)s_pet_individual_constraint'),
        )


class PetPhotoAlbum(models.Model):
    """ Class album with photos, for individual pets. Includes meta information about the photo.
    """
    pet = models.ForeignKey(Cats, on_delete=models.CASCADE, verbose_name=_('pet'))
    title = models.CharField(max_length=30, verbose_name=_('title'), default='')
    photo = models.ImageField(
        verbose_name=_('photo'),
        height_field='img_height',
        width_field='img_width',
        upload_to=upload_into_album,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image]
    )
    img_height = models.PositiveIntegerField(verbose_name=_('height'))
    img_width = models.PositiveIntegerField(verbose_name=_('width'))

    def __str__(self):
        return f'{self.title}:{self.img_width}x{self.img_height}px'
