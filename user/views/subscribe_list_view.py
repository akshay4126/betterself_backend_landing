from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from user.models import SubscribeList
from user.serializers.subscribe_list_serializer import SubscribeListSerializer


class SubscribeListView(CreateModelMixin, GenericViewSet):
    queryset = SubscribeList.objects.all()
    serializer_class = SubscribeListSerializer
