from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import (
    Contact,
    ContactSubject,
    NewsLetter,
)

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        exclude = ('imported', )
        fields = ('name', 'email', 'phone', 'subject', 'message', 'terms')
        export_order = ('name', 'email', 'phone', 'subject', 'message', 'terms')

class ContactAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ContactResource
    to_encoding = 'utf-8'

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactSubject)

class NewsLetterResource(resources.ModelResource):
    class Meta:
        model = NewsLetter
        exclude = ('imported', )
        fields = ('nome', 'email', 'termos')
        export_order = ('nome', 'email', 'termos')

class NewsLetterAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = NewsLetterResource
    to_encoding = 'utf-8'

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(NewsLetter, NewsLetterAdmin)