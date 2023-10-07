from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import (
    GenericPrivacyPolicyPlugin4,
    GenericTermsAndConditionsPlugin5,
    NewsLetter,
    ImagesResized,
    GenericHeaderPlugin1,
    GenericFooterPlugin2
)

admin.site.register(GenericPrivacyPolicyPlugin4)
admin.site.register(GenericTermsAndConditionsPlugin5)
admin.site.register(ImagesResized)
admin.site.register(GenericHeaderPlugin1)
admin.site.register(GenericFooterPlugin2)

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
