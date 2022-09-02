import pytest

from src.cats .models import Cats


@pytest.mark.django_db
def test_create_pet():
    """ test: create pet and check model Cats """
    pet = Cats.objects.create(
        name="Plush",
        birthday="2020-01-07",
        color="White with orange",
        temperament="",
        description="Eat and sleep"
    )
    assert pet.name == "Plush"
    assert pet.birthday == "2020-01-07"
    assert pet.color == "White with orange"
    assert pet.description == "Eat and sleep"
