import os
from shutil import rmtree

from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from django.core.cache import cache
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from common.utils import TEST_PATH, random_string
from user.models import User
from user.tests.factories import UserFactory


class BaseTestCase(TestCase):
    def tearDown(self):
        assert 'test' in settings.MEDIA_ROOT_TEST
        rmtree(settings.MEDIA_ROOT_TEST, ignore_errors=True)

    @staticmethod
    def create_test_file(name=None, content='test'):
        name = name or f'testfile_{random_string()}.txt'
        path = os.path.join(TEST_PATH, name)
        if not os.path.exists(TEST_PATH):
            os.makedirs(TEST_PATH)
        with open(path, 'w') as f:
            f.write(content)
        return path


class BaseViewTests(BaseTestCase, APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cache.clear()

    def _test_private_actions(self, view_name, actions=None):
        url_list = reverse(f'{view_name}-list')
        url_detail = reverse(f'{view_name}-detail', kwargs={'pk': 1})
        actions_map = {
            'create': (self.client.post, url_list),
            'list': (self.client.get, url_list),
            'retrieve': (self.client.post, url_detail),
            'patch': (self.client.post, url_detail),
            'put': (self.client.post, url_detail),
            'delete': (self.client.post, url_detail)
        }
        private_actions = actions_map if not actions else {k: v for (k, v) in actions_map.items() if k in actions}
        for request, url in private_actions.values():
            response = request(url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def login_as_admin(self):
        qs = User.objects.filter(is_active=True, is_staff=True)
        if qs.exists():
            admin_user = qs.first()
        else:
            admin_user = UserFactory(is_active=True, is_staff=True)
        self.client.force_authenticate(admin_user)
