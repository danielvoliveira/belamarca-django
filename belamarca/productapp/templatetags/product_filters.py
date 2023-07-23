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
    selected_types = request.GET.get('types', '')
    selected_colors = request.GET.get('colors', '')
    selected_prints = request.GET.get('prints', '')
    selected_materials = request.GET.get('materials', '')

    if selected_categories != '':
        selected_categories = ast.literal_eval(selected_categories)
    else:
        selected_categories = []

    if selected_sizes != '':
        selected_sizes = ast.literal_eval(selected_sizes)
    else:
        selected_sizes = []

    if selected_types != '':
        selected_types = ast.literal_eval(selected_types)
    else:
        selected_types = []

    if selected_colors != '':
        selected_colors = ast.literal_eval(selected_colors)
    else:
        selected_colors = []

    if selected_prints != '':
        selected_prints = ast.literal_eval(selected_prints)
    else:
        selected_prints = []

    if selected_materials != '':
        selected_materials = ast.literal_eval(selected_materials)
    else:
        selected_materials = []

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
    final_types = []
    final_colors = []
    final_prints = []
    final_materials = []

    for attribute in attributes:
        # Regra para ordenar filtros de "Estampa" e "Cores"
        if attribute.name == 'Tamanho':
            attribute_options = AttributeOption.objects.filter(attribute=attribute, disp='disponivel')
        else:
            attribute_options = AttributeOption.objects.filter(attribute=attribute, disp='disponivel').order_by('name')

        for attribute_option in attribute_options:
            selected = ''

            if attribute.name == 'Tamanho':
                if attribute_option.id in selected_sizes:
                    selected = 'selected'

                final_sizes.append({
                    'id': attribute_option.id,
                    'name': attribute_option.name,
                    'text': attribute_option.text,
                    'selected': selected,
                })

            if attribute.name == 'Tecído':
                if attribute_option.id in selected_materials:
                    selected = 'selected'

                final_materials.append({
                    'id': attribute_option.id,
                    'name': attribute_option.name,
                    'text': attribute_option.text,
                    'selected': selected,
                })

            if attribute.name == 'Tipo':
                if attribute_option.id in selected_types:
                    selected = 'selected'

                final_types.append({
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
                else:
                    final_prints.append({
                        'id': attribute_option.id,
                        'name': attribute_option.name,
                        'image': {
                            'url': '',
                            'alt': 'Estampa {}'.format(attribute_option.name),
                        },
                        'selected': selected,
                    })

    return {
        'categories': final_categories,
        'sizes': final_sizes,
        'types': final_types,
        'colors': final_colors,
        'prints': final_prints,
        'materials': final_materials,
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
