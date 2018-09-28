from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from common.models import WebContent, WebContentEditor
from common.serializers import WebContentSerializer, WebContentEditorSerializer


class WebContentView(ListModelMixin, GenericViewSet):
    queryset = WebContent.objects.all()
    serializer_class = WebContentSerializer


class WebContentEditorView(ListModelMixin, GenericViewSet):
    queryset = WebContentEditor.objects.all()
    serializer_class = WebContentEditorSerializer
    filter_fields = ['key']
