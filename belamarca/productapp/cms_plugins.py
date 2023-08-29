from pyexpat import model
from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from genericapp.models import (
    ImagesResized,
)

from .models import (
    Category,
    Product,
    ProductPrice,
    ProductCategoryGrid,
    ProductCarrossel,
    Disponibility,
)

# ------------------------------------------
# 1 - Produtos - Grid de Produtos
# ------------------------------------------

@plugin_pool.register_plugin
class ProductGridPlugin1(CMSPluginBase):
    module = 'Produto'
    name = '01 - Produtos - Grid de Produtos'
    render_template = "productapp/product_list.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        products = Product.objects.filter(disp='disponivel').order_by('-id')

        for product in products:
            #Pegando preço dos produtos
            product_price = ProductPrice.objects.filter(id_product=product).get()
            product.price = product_price.price

        context.update({
            'instance': instance,
            'products': products,
        })
        return context

# ------------------------------------------
# 2 - Produtos - Categoria de produtos
# ------------------------------------------

@plugin_pool.register_plugin
class ProductCategoryPlugin2(CMSPluginBase):
    module = 'Produto'
    name = '02 - Produtos - Categoria de produtos'
    render_template = "productapp/product_category.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        products = Product.objects.filter(disp='disponivel').order_by('-id')

        for product in products:
            #Pegando preço dos produtos
            product_price = ProductPrice.objects.filter(id_product=product).get()
            product.price = product_price.price

        context.update({
            'instance': instance,
            'products': products,
        })
        return context

# ------------------------------------------
# 04 - Grid de Categorias
# ------------------------------------------

@plugin_pool.register_plugin
class ProductGridCategory(CMSPluginBase):
    module = 'Produto'
    name = '03 - Produtos - Grid de Categorias'
    model = ProductCategoryGrid
    render_template = "productapp/product_grid_category.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        products = Product.objects.filter(disp='disponivel').order_by('-id')

        for product in products:
            #Pegando preço dos produtos
            product_price = ProductPrice.objects.filter(id_product=product).get()
            product.price = product_price.price

        context.update({
            'instance': instance,
            'products': products,
        })
        return context

# ------------------------------------------
# 05 - Produtos - Carrosel de Produtos
# ------------------------------------------

@plugin_pool.register_plugin
class ProductCarroselPlugin5(CMSPluginBase):
    module = 'Produto'
    name = '04 - Produtos - Carrossel de Produtos'
    model = ProductCarrossel
    render_template = "productapp/product_carrossel.html"
    allow_children = False

    fieldsets = [
        ('Bloco Principal', {
            'fields': (
                ('title'),
                ('subtitle'),
                # ('text_color'),
                ('show_only'),
                ('categories'),
                ('subcategories'),
                ('attributes'),
                ('attribute_options'),
                ('products'),
            )
        }),
    ]

    def render(self, context, instance, placeholder):

        if instance.show_only == 'category':
            carrossel_products = Product.objects.filter(
                category__in=instance.categories.all(),
                productimage__isnull=False, # Apenas produtos que tenham imagem
                productprice__price__gt=0, # Apenas produtos com preço > 0
                disp='disponivel'
            ).order_by('?')[:12]

        elif instance.show_only == 'subcategory':
            carrossel_products = Product.objects.filter(
                subcategory__id__in=instance.subcategories.all(),
                productimage__isnull=False, # Apenas produtos que tenham imagem
                productprice__price__gt=0, # Apenas produtos com preço > 0
                disp='disponivel'
            ).order_by('?')[:12]

        elif instance.show_only == 'attribute':
            carrossel_products = Product.objects.filter(
                attribute_options__attribute__in=instance.attributes.all(),
                productimage__isnull=False, # Apenas produtos que tenham imagem
                productprice__price__gt=0, # Apenas produtos com preço > 0
                disp='disponivel'
            ).order_by('?')[:12]

        elif instance.show_only == 'attribute_option':
            carrossel_products = Product.objects.filter(
                attribute_options__id__in=instance.attribute_options.all(),
                productimage__isnull=False, # Apenas produtos que tenham imagem
                productprice__price__gt=0, # Apenas produtos com preço > 0
                disp='disponivel'
            ).order_by('?')[:12]

        elif instance.show_only == 'product':
            carrossel_products = instance.products.filter(
                productimage__isnull=False, # Apenas produtos que tenham imagem
                productprice__price__gt=0, # Apenas produtos com preço > 0
                disp='disponivel'
            ).order_by('?')[:12]

        for product in carrossel_products:
            #Pegando preço dos produtos
            product_price = ProductPrice.objects.filter(id_product=product).get()
            product.price = product_price.price

        context.update({
            'instance': instance,
            'products': carrossel_products,
        })
        return context