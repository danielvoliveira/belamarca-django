from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from .models import (
    SeoMetaTags,
    GoogleCorporationMetaTag,
    GoogleProductListMetaTag,
    GoogleProductMetaTag,
)

# ----------------------------------------
# SEO Meta Tags para criar os modelos de
# Google Meta Tag adequado para cada path
# ----------------------------------------

@receiver(post_save, sender=SeoMetaTags)
def create_google_corporation_meta_tag(sender, instance, created, **kwargs):
    if created:
        if instance.path == 'produtos':
            GoogleProductListMetaTag.objects.create(seo_meta_tags=instance)
        elif instance.path == 'produto':
            GoogleProductMetaTag.objects.create(seo_meta_tags=instance)
        else:
            GoogleCorporationMetaTag.objects.create(seo_meta_tags=instance)

post_save.connect(create_google_corporation_meta_tag, sender=SeoMetaTags)
