from django.contrib import admin

from common.models import WebContent


@admin.register(WebContent)
class WebContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'date_modified')
    search_fields = ('key', 'text')
    readonly_fields = ('key', 'date_modified')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
