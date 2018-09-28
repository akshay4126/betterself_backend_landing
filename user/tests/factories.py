import factory

from user.models import User
from common.utils import random_string


def test_email():
    return f'{random_string()}@test.com'


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyFunction(test_email)
