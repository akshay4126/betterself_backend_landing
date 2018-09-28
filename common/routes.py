from rest_framework import routers

from common.views import WebContentView


common_router = routers.SimpleRouter()
common_router.register('web_content/blocks', WebContentView, 'web-content')
