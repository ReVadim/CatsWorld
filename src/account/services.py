import os

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """ Building a file path, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def validate_size_image(file_obj):
    """ Checking file size
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")
