from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from mainsite.utils.image_resizer import (
    create_images_resized_signals,
    delete_images_resized_signals,
)

from mainsite.utils.image_resizer_to_image_field import (
    create_image_resizer_to_image_field,
    delete_image_resizer_to_image_field,
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
def create_attribute_option_image(sender, instance, **kwargs):
    create_image_resizer_to_image_field(
        instance,
        model=AttributeOption,
        final_field_name='p2_image_image_resize',
        final_field_size='p2_image_image_size',
    )


@receiver(post_delete, sender=AttributeOption)
def delete_attribute_option_image(sender, instance, **kwargs):
    delete_image_resizer_to_image_field(
        instance,
        model=AttributeOption,
        final_field_name='p2_image_image_resize',
    )

# ----------------------------------------
# 03 - Produtos
# ----------------------------------------

@receiver(post_save, sender=ProductImage)
def create_product_image(sender, instance, **kwargs):
    create_image_resizer_to_image_field(
        instance,
        model=ProductImage,
        final_field_name='p3_image_resize',
        final_field_size='p3_image_size',
    )

@receiver(post_delete, sender=ProductImage)
def delete_product_image(sender, instance, **kwargs):
    delete_image_resizer_to_image_field(
        instance,
        model=ProductImage,
        final_field_name='p3_image_resize',
    )