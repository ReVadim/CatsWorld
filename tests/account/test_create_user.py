import pytest

from src.account.models import CatsUser


@pytest.mark.django_db
def test_create_user():
    """ test: create user """
    user = CatsUser.objects.create(
        is_activated=True,
        email='test_user_first@email.com',
        country='Russia',
        city='CatsBurg',
        about='Mew, my name is Kitty',
        username='Kitty'
    )
    assert user.email == 'test_user_first@email.com'
    assert user.city == 'CatsBurg'
    assert user.username == 'Kitty'
