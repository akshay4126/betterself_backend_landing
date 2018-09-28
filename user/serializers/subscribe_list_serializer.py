from rest_framework import serializers

from user.models import SubscribeList


class SubscribeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeList
        fields = ['email', 'date_created']
        read_only_fields = ['date_created']

    def create(self, validated_data):
        instance, _ = SubscribeList.objects.get_or_create(email=validated_data['email'])
        return instance
