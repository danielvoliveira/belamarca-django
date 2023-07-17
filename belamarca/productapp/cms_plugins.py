from itertools import product
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