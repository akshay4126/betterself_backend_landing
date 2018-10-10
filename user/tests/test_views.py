from unittest.mock import patch

from django.urls import reverse
from rest_framework import status

from common.tests import BaseViewTests
from common.utils import random_string, random_email
from user.models import ContactForm


class SubscribeListViewTests(BaseViewTests):
    @patch('user.tasks.new_subscribe_list_mail.delay')
    def test_create(self, mock_obj):
        url = reverse('subscribe-list-list')
        data = {'email': random_email()}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertIsNotNone(response.data.get('date_created'))
        recipients = [data['email']]
        mock_obj.assert_called_once_with(recipients)


class ContactFormViewTests(BaseViewTests):
    @patch('user.tasks.contact_us_admin_mail.delay')
    def test_create(self, mock_obj):
        url = reverse('contact-form-list')
        data = {'email': random_email(), 'name': random_string(), 'message': random_string()}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['message'], data['message'])
        self.assertIsNotNone(response.data.get('date_created'))
        created_pk = ContactForm.objects.get(email=data['email']).pk
        mock_obj.assert_called_once_with(created_pk)
