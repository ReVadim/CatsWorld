from django.template.loader import render_to_string
from config.settings import ALLOWED_HOSTS
from django.core.signing import Signer
from django.core.exceptions import ValidationError


signer = Signer()


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


def send_activation_notification(user):
    """ Send activation notification to user email
    """
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)


def get_path_upload_photo(instance, file):
    """ Building a file path, format: (media)/photos/user_id/photo.jpg
    """
    return f'photos/user_{instance.id}/{file}'
