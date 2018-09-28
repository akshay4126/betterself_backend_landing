from rest_framework import serializers

from common.models import WebContent, WebContentEditor


class WebContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebContent
        fields = ['key', 'text', 'image', 'date_modified']
        read_only_fields = fields


class WebContentEditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebContentEditor
        fields = ['key', 'content', 'date_modified']
        read_only_fields = fields
