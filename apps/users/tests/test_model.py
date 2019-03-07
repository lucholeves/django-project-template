import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_create_user():
    user = mixer.blend('users.User')

    assert user.pk, "No se pudo crear un usuario"
