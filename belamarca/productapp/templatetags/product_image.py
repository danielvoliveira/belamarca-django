from django import template
from django.template.loader import get_template
from cms.models.pagemodel import Page
from genericapp.models import ImagesResized
from productapp.models import (
    ProductImage,
)

def change_http_to_https(url):
    if 'http://' in url:
        url = url.replace('http://', 'https://')

    return url

register = template.Library()

@register.filter
def product_image(product):
    product_images = ProductImage.objects.filter(product_id=product)[:1]

    resized_images_url = []
    images = []
    for image in product_images:
        model_name = ProductImage.__name__
        resized_images = None

        if ImagesResized.objects.filter(model_id=image.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=image.id, model_name=model_name
            )

            resized_images_url.append({
                'desktop': resized_images[0].image_desktop.url,
                'tablet': resized_images[0].image_tablet.url,
                'mobile': resized_images[0].image_mobile.url,
                'alt': image.alt,
            })

        images.append({
            'path' : image.p3_image_resize,
            'alt': image.alt,
        })

    return {
        'images': images,
        'resized_images': resized_images_url,
    }

# {% load product_image %}

# {% with product_image=product|product_image %}
#     {% for image in product_image.images %}
#         <img src="{% get_media_prefix %}{{ image.path }}" alt="{{ image.alt }}">
#     {% endfor %}
# {% endwith %}
