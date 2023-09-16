from django.contrib import admin

from .models import (
    SeoSinglePagePlugin1,
    SeoMetaTags,
)

from .models import (
    SeoMetaTags,
    GoogleCorporationMetaTag,
    GoogleProductListMetaTag,
    GoogleProductMetaTag,
)
from .forms import (
    SeoMetaTagsForm,
    GoogleCorporationMetaTagForm,
    GoogleProductListMetaTagForm,
    GoogleProductMetaTagForm,
)

admin.site.register(SeoSinglePagePlugin1)

class GoogleCorporationMetaTagInline(admin.StackedInline):
    model = GoogleCorporationMetaTag
    form = GoogleCorporationMetaTagForm
    extra = 0  # Number of empty forms to display

class GoogleProductListMetaTagInline(admin.StackedInline):
    model = GoogleProductListMetaTag
    form = GoogleProductListMetaTagForm
    extra = 0  # Number of empty forms to display

class GoogleProductMetaTagInline(admin.StackedInline):
    model = GoogleProductMetaTag
    form = GoogleProductMetaTagForm
    extra = 0  # Number of empty forms to display

@admin.register(SeoMetaTags)
class SeoMetaTagsAdmin(admin.ModelAdmin):
    form = SeoMetaTagsForm
    inlines = [
        GoogleCorporationMetaTagInline,
        GoogleProductListMetaTagInline,
        GoogleProductMetaTagInline,
    ]