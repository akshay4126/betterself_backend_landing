from rest_framework import routers

from common.views import WebContentView, WebContentEditorView


common_router = routers.SimpleRouter()
common_router.register('web_content/blocks', WebContentView, 'web-content-blocks')
common_router.register('web_content/editor', WebContentEditorView, 'web-content-editor')
