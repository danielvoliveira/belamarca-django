from django import template
from django.template.loader import get_template
from cms.models.pagemodel import Page
from genericapp.models import ImagesResized
from productapp.models import (
    ProductPrice,
    ProductImage,
)

def change_http_to_https(url):
    if 'http://' in url:
        url = url.replace('http://', 'https://')

    return url

register = template.Library()

@register.filter
def product_detail(product):
    #Pegando preço dos produtos
    product_price = ProductPrice.objects.filter(id_product=product).get()

    #Pegando imagem dos produtos
    product_images = ProductImage.objects.filter(product_id=product)

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
        'price': "{:.2f}".format(product_price.price),
        'images': images,
        'resized_images': resized_images_url,
    }

#{% load product_detail %}
#{% with product_detail=object|product_detail %}
#    {% if product_detail != False %}
#        {{ product_detail.price }}
#    {% endif %}
#{% endwith %}

#{% for image in product_detail.images %}
#    <img src="{% get_media_prefix %}{{ image.path }}" alt="{{ image.alt }}">
#{% endfor %}
