from rest_framework import serializers

from user.models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['email', 'name', 'message', 'date_created']
        read_only_fields = ['date_created']
