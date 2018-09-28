from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from user.models import ContactForm
from user.serializers.contact_form_serializer import ContactFormSerializer


class ContactFormView(CreateModelMixin, GenericViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
