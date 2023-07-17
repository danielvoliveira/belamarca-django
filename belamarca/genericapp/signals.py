from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from mainsite.utils.image_resizer import (
    create_images_resized_signals,
    delete_images_resized_signals,
)

from .models import (
    GenericHeaderPlugin1,
    GenericFooterPlugin2,
    GenericIconsPlugin3,
)

# ----------------------------------------
# 1 - Cabeçalho - Logo, menu com submenu e botão
# ----------------------------------------


@receiver(post_save, sender=GenericHeaderPlugin1)
def create_generic_header_plugin1(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=GenericHeaderPlugin1,
    )


@receiver(post_delete, sender=GenericHeaderPlugin1)
def delete_generic_header_plugin1(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=GenericHeaderPlugin1,
    )

# ------------------------------------------------------------
# 2 - Rodapé - Logo, redes sociais, links úteis e assinatura
# ------------------------------------------------------------


@receiver(post_save, sender=GenericFooterPlugin2)
def create_generic_footer_plugin2(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=GenericFooterPlugin2,
    )


@receiver(post_delete, sender=GenericFooterPlugin2)
def delete_generic_footer_plugin2(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=GenericFooterPlugin2,
    )

# ------------------------------------------------------------
# 3 - Ícones Flutuantes - Voltar ao topo e whatsapp
# ------------------------------------------------------------


@receiver(post_save, sender=GenericIconsPlugin3)
def create_generic_icons_plugin3(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=GenericIconsPlugin3,
    )


@receiver(post_delete, sender=GenericIconsPlugin3)
def delete_generic_icons_plugin3(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=GenericIconsPlugin3,
    )
