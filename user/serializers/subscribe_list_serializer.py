from rest_framework import serializers

from user.models import SubscribeList


class SubscribeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeList
        fields = ['email', 'date_created']
        read_only_fields = ['date_created']
