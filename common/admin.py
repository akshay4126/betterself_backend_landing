from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from common.models import WebContent, WebContentEditor


@admin.register(WebContent)
class WebContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'date_modified')
    search_fields = ('key', 'text')
    readonly_fields = ('key', 'date_modified')
    exclude = ('image', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class WebContentEditorAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = WebContentEditor
        fields = '__all__'


@admin.register(WebContentEditor)
class WebContentEditorAdmin(admin.ModelAdmin):
    form = WebContentEditorAdminForm
    list_display = ('key', 'date_modified')
    search_fields = ('key', )
    readonly_fields = ('key', 'date_modified')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
