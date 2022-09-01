from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.base.services import get_path_upload_photo, validate_size_image


class Cats(models.Model):
    """ Main model include all information about cats
    """
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
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    def __str__(self):
        return f"{self.temperament} {self.name}"

    class Meta:
        verbose_name = _('pet')
        verbose_name_plural = _('pets')
