from django.core.management import BaseCommand

from common.models import WebContent
from common.constants import WEB_CONTENT_BLOCKS


class Command(BaseCommand):
    def handle(self, *args, **options):
        for fx in WEB_CONTENT_BLOCKS:
            WebContent.objects.get_or_create(**fx)
