from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from common.models import WebContent
from common.serializers import WebContentSerializer


class WebContentView(ListModelMixin, GenericViewSet):
    queryset = WebContent.objects.all()
    serializer_class = WebContentSerializer
