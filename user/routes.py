from rest_framework import routers

from user.views.contact_form_view import ContactFormView
from user.views.subscribe_list_view import SubscribeListView


user_router = routers.SimpleRouter()
user_router.register('subscribe_list', SubscribeListView, 'subscribe-list')
user_router.register('contact_form', ContactFormView, 'contact-form')
