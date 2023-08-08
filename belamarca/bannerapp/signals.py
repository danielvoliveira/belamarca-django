from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from mainsite.utils.image_resizer import (
    create_images_resized_signals,
    delete_images_resized_signals,
)

from .models import (
    BannerPlugin1,
    BannerPlugin2,
    BannerPlugin3,
    BannerPlugin4,
)


#------------------------------------------------------
# 1 - Página Inicial - Título, subtítulo e botão
#------------------------------------------------------

@receiver(post_save, sender=BannerPlugin1)
def create_banner_plugin_1(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=BannerPlugin1,
    )

@receiver(post_delete, sender=BannerPlugin1)
def delete_banner_plugin_1(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=BannerPlugin1,
    )

#------------------------------------------------------
# 2 - Atrações - Imagem na esquerda; título e subtítulo na direita 2
#------------------------------------------------------

@receiver(post_save, sender=BannerPlugin2)
def create_banner_plugin_2(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=BannerPlugin2,
    )

@receiver(post_delete, sender=BannerPlugin2)
def delete_banner_plugin_2(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=BannerPlugin2,
    )

#------------------------------------------------------
# 3 - Atrações - Imagem na esquerda; título e subtítulo na direita 2
#------------------------------------------------------

@receiver(post_save, sender=BannerPlugin3)
def create_banner_plugin_3(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=BannerPlugin3,
    )

@receiver(post_delete, sender=BannerPlugin3)
def delete_banner_plugin_3(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=BannerPlugin3,
    )

@receiver(post_save, sender=BannerPlugin4)
def create_banner_plugin_4(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=BannerPlugin4,
    )

@receiver(post_delete, sender=BannerPlugin4)
def delete_banner_plugin_4(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=BannerPlugin4,
    )
