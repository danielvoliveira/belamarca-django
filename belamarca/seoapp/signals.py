from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from .models import (
    SeoMetaTags,
    GoogleWebSiteMetaTag,
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
            GoogleProductListMetaTag.objects.create(seo_meta_tags=instance)
            GoogleCorporationMetaTag.objects.create(seo_meta_tags=instance)
        elif '/produto/' in instance.path:
            GoogleProductMetaTag.objects.create(seo_meta_tags=instance)
            GoogleCorporationMetaTag.objects.create(seo_meta_tags=instance)
        else:
            GoogleWebSiteMetaTag.objects.create(seo_meta_tags=instance)
            GoogleCorporationMetaTag.objects.create(seo_meta_tags=instance)
        instance.save()
    else:
        # Criando GoogleWebSiteMetaTag somente para páginas que não são de produto
        if (
            instance.path != '/produtos/' and
            '/produto/' not in instance.path
        ):
            web_site_tag, created_web_site = GoogleWebSiteMetaTag.objects.get_or_create(seo_meta_tags=instance)
            if not created_web_site:
                web_site_tag.save()

        # Criando GoogleCorporationMetaTag em todos os tipos de página
        corporation_tag, created_corporation = GoogleCorporationMetaTag.objects.get_or_create(seo_meta_tags=instance)
        if not created_corporation:
            corporation_tag.save()

        # Criando GoogleProductListMetaTag somente na página de listagem de produtos
        if instance.path == '/produtos/':
            product_list_tag, created_product_list = GoogleProductListMetaTag.objects.get_or_create(seo_meta_tags=instance)
            if not created_product_list:
                product_list_tag.save()

        # Criando GoogleProductMetaTag somente na página de exibição de um produto
        if '/produto/' in instance.path:
            product_tag, created_product = GoogleProductMetaTag.objects.get_or_create(seo_meta_tags=instance)
            if not created_product:
                product_tag.save()

post_save.connect(create_google_corporation_meta_tag, sender=SeoMetaTags)
