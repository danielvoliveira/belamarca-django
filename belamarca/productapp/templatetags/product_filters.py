from dis import dis
from unicodedata import category
from django import template
from django.template.loader import get_template
from cms.models.pagemodel import Page
import ast
from genericapp.models import ImagesResized
from productapp.models import (
    Category,
    Attribute,
    AttributeOption,
)

register = template.Library()

#http://localhost:8080/produtos/?categories=[1,2,3]&sizes=[1,2,3]&colors=[1,2,3]&prints=[1,2,3]

@register.filter
def product_filters(request):
    selected_categories = request.GET.get('categories', '')
    selected_sizes = request.GET.get('sizes', '')
    selected_colors = request.GET.get('colors', '')
    selected_prints = request.GET.get('prints', '')

    if selected_categories is not '':
        selected_categories = ast.literal_eval(selected_categories)
    else:
        selected_categories = []

    if selected_sizes is not '':
        selected_sizes = ast.literal_eval(selected_sizes)
    else:
        selected_sizes = []

    if selected_colors is not '':
        selected_colors = ast.literal_eval(selected_colors)
    else:
        selected_colors = []

    if selected_prints is not '':
        selected_prints = ast.literal_eval(selected_prints)
    else:
        selected_prints = []

    categories = Category.objects.filter(disp='disponivel').order_by('name')
    final_categories = []

    for category in categories:
        selected = ''
        if category.id in selected_categories:
            selected = 'selected'

        final_categories.append({
            'id': category.id,
            'name': category.name,
            'selected': selected,
        })

    attributes = Attribute.objects.filter(disp='disponivel')
    final_sizes = []
    final_colors = []
    final_prints = []

    for attribute in attributes:
        attribute_options = AttributeOption.objects.filter(attribute=attribute, disp='disponivel')

        for attribute_option in attribute_options:
            selected = ''
            attribute_name = attribute.name.lower()

            if attribute.name == 'Tamanho':
                if attribute_option.id in selected_sizes:
                    selected = 'selected'

                final_sizes.append({
                    'id': attribute_option.id,
                    'name': attribute_option.name,
                    'text': attribute_option.text,
                    'selected': selected,
                })

            if attribute.name == 'Cor':
                if attribute_option.id in selected_colors:
                    selected = 'selected'

                final_colors.append({
                    'id': attribute_option.id,
                    'name': attribute_option.name,
                    'color': attribute_option.color,
                    'selected': selected,
                })

            if attribute.name == 'Estampa':
                if attribute_option.id in selected_prints:
                    selected = 'selected'

                resized_images_url = []
                model_name = AttributeOption.__name__
                resized_images = None

                if ImagesResized.objects.filter(model_id=attribute_option.id, model_name=model_name).exists():
                    resized_images = ImagesResized.objects.filter(
                        model_id=attribute_option.id, model_name=model_name
                    )

                    # resized_images_url.append({
                    #     'desktop': resized_images[0].image_desktop.url,
                    #     'tablet': resized_images[0].image_tablet.url,
                    #     'mobile': resized_images[0].image_mobile.url,
                    #     'alt': 'Estampa {}'.format(attribute_option.name),
                    # })

                    final_prints.append({
                        'id': attribute_option.id,
                        'name': attribute_option.name,
                        'image': {
                            'url': resized_images[0].image_desktop.url,
                            'alt': 'Estampa {}'.format(attribute_option.name),
                        },
                        'selected': selected,
                    })

    return {
        'categories': final_categories,
        'sizes': final_sizes,
        'colors': final_colors,
        'prints': final_prints,
        'prices': {
            'max-price': '1000',
            'min-price': '200',
            },
    }

# {% load product_image %}

# {% with product_image=product|product_image %}
#     {% for image in product_image.images %}
#         <img src="{% get_media_prefix %}{{ image.path }}" alt="{{ image.alt }}">
#     {% endfor %}
# {% endwith %}
