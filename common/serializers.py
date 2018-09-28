from rest_framework import serializers

from common.models import WebContent


class WebContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebContent
        fields = ['key', 'text', 'image', 'date_modified']
        read_only_fields = fields
