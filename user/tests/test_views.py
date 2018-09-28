from django.urls import reverse
from rest_framework import status

from common.tests import BaseViewTests
from common.utils import random_string, random_email


class SubscribeListViewTests(BaseViewTests):
    def test_create(self):
        url = reverse('subscribe-list-list')
        data = {'email': random_email()}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertIsNotNone(response.data.get('date_created'))


class ContactFormViewTests(BaseViewTests):
    def test_create(self):
        url = reverse('contact-form-list')
        data = {'email': random_email(), 'name': random_string(), 'message': random_string()}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['message'], data['message'])
        self.assertIsNotNone(response.data.get('date_created'))
