import django
django.setup()
import pytest
from rest_framework.test import APIClient

from core.account.models import User


@pytest.fixture(scope='session')
def api_client():
    return APIClient()


@pytest.fixture
def admin():
    user = User(
        email='admin@gmail.com',
        name='admin',
        is_superuser=True,
        is_staff=True,
    )
    user.set_password('123')
    user.save()
    return user