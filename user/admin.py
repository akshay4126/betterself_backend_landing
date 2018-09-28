from django.contrib import admin

from user.models import ContactForm, SubscribeList


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    search_fields = ('email', 'name')
    readonly_fields = ('date_created', )


@admin.register(SubscribeList)
class SubscribeListAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_created')
    search_fields = ('email',)
    readonly_fields = ('date_created', 'token', 'invited')
