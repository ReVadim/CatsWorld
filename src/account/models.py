from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from ..base.services import (
    get_path_upload_avatar,
    validate_size_image,
)


class CatsOwner(AbstractUser):
    """ Custom user model
    """
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    username_validator = UnicodeUsernameValidator()

    is_activated = models.BooleanField(default=True, db_index=True, verbose_name=_("is activated?"))
    send_message = models.BooleanField(default=True, verbose_name=_("send messages?"))
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("country"))
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("city"))
    about = models.TextField(max_length=2000, blank=True, null=True)
    username = models.CharField(
        max_length=30, blank=True, null=True, verbose_name=_("username"), validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")}
    )
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        verbose_name=_("avatar"),
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image]
    )

    def __str__(self):
        return f'{self.email} - {self.username}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
