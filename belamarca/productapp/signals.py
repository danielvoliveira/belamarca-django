from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from mainsite.utils.image_resizer import (
    create_images_resized_signals,
    delete_images_resized_signals,
)

from mainsite.utils.product_image_resizer import (
    create_product_image_resizer,
    delete_product_image_resizer,
)

from .models import (
    Category,
    AttributeOption,
    ProductImage,
)

# ----------------------------------------
# 01 - Category
# ----------------------------------------


# @receiver(post_save, sender=Category)
# def create_category_image(sender, instance, **kwargs):
#     create_images_resized_signals(
#         instance,
#         model=Category,
#     )


# @receiver(post_delete, sender=Category)
# def delete_category_image(sender, instance, **kwargs):
#     delete_images_resized_signals(
#         instance,
#         model=Category,
#     )

# ----------------------------------------
# 02 - Atributos
# ----------------------------------------


@receiver(post_save, sender=AttributeOption)
def create_generic_header_plugin1(sender, instance, **kwargs):
    create_images_resized_signals(
        instance,
        model=AttributeOption,
    )


@receiver(post_delete, sender=AttributeOption)
def delete_generic_header_plugin1(sender, instance, **kwargs):
    delete_images_resized_signals(
        instance,
        model=AttributeOption,
    )

# ----------------------------------------
# 03 - Produtos
# ----------------------------------------

@receiver(post_save, sender=ProductImage)
def create_product_image(sender, instance, **kwargs):
    create_product_image_resizer(
        instance,
        model=ProductImage,
    )

@receiver(post_delete, sender=ProductImage)
def delete_product_image(sender, instance, **kwargs):
    delete_product_image_resizer(
        instance,
        model=ProductImage,
    )