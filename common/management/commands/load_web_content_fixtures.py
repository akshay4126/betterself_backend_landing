from django.core.management import BaseCommand

from common.models import WebContent, WebContentEditor
from common.constants import WEB_CONTENT_BLOCKS, WEB_CONTENT_EDITOR


class Command(BaseCommand):
    def handle(self, *args, **options):
        for fx in WEB_CONTENT_BLOCKS:
            WebContent.objects.get_or_create(**fx)
        for fx in WEB_CONTENT_EDITOR:
            WebContentEditor.objects.get_or_create(**fx)
