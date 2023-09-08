from django.contrib import admin

from .models import (
    SeoSinglePagePlugin1,
    SeoMetaTags,
)

admin.site.register(SeoMetaTags)
admin.site.register(SeoSinglePagePlugin1)
