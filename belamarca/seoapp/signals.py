from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from .models import (
    SeoMetaTags,
    GoogleCorporationMetaTag,
    GoogleProductListMetaTag,
    GoogleProductMetaTag,
    GoogleType,
)

# ----------------------------------------
# SEO Meta Tags para criar os modelos de
# Google Meta Tag adequado para cada path
# ----------------------------------------

@receiver(post_save, sender=SeoMetaTags)
def create_google_corporation_meta_tag(sender, instance, created, **kwargs):
    if created:
        if instance.path == '/produtos/':
            instance.google_type = GoogleType.PRODUCT_LIST
            GoogleProductListMetaTag.objects.create(seo_meta_tags=instance)
        elif '/produto/' in instance.path:
            instance.google_type = GoogleType.PRODUCT
            GoogleProductMetaTag.objects.create(seo_meta_tags=instance)
        else:
            instance.google_type = GoogleType.CORPORATION
            GoogleCorporationMetaTag.objects.create(seo_meta_tags=instance)
        instance.save()
    else:
        if(
            instance.google_type == 'Corporation' or
            instance.google_type == 'Organization'
        ):
            corporation_tag, created_corporation = GoogleCorporationMetaTag.objects.get_or_create(seo_meta_tags=instance)
            if not created_corporation:
                corporation_tag.save()

            GoogleProductListMetaTag.objects.filter(seo_meta_tags=instance).delete()
            GoogleProductMetaTag.objects.filter(seo_meta_tags=instance).delete()
        elif instance.google_type == 'product_list':
            product_list_tag, created_product_list = GoogleProductListMetaTag.objects.get_or_create(seo_meta_tags=instance)
            if not created_product_list:
                product_list_tag.save()

            GoogleCorporationMetaTag.objects.filter(seo_meta_tags=instance).delete()
            GoogleProductMetaTag.objects.filter(seo_meta_tags=instance).delete()
        elif instance.google_type == 'product':
            product_tag, created_product = GoogleProductMetaTag.objects.get_or_create(seo_meta_tags=instance)
            if not created_product:
                product_tag.save()

            GoogleCorporationMetaTag.objects.filter(seo_meta_tags=instance).delete()
            GoogleProductListMetaTag.objects.filter(seo_meta_tags=instance).delete()

post_save.connect(create_google_corporation_meta_tag, sender=SeoMetaTags)
