from mainsite.utils.external_and_internal_link import (
    get_link,
    get_form,
    for_site,
)
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from genericapp.models import (
    ImagesResized,
)

from .models import (
    BannerPlugin1,
    BannerPlugin2,
    BannerPlugin3,
)

from .forms import (
    BannerPlugin1Form,
    BannerPlugin2Form,
    BannerPlugin3Form,
)


#------------------------------------------------------
# 1 - Banner
#------------------------------------------------------

@plugin_pool.register_plugin
class BannerPlugin1(CMSPluginBase):
    module = 'Banner'
    model = BannerPlugin1
    form = BannerPlugin1Form
    name = "01 - Banner - Título e subtítulo centralizados com imagem de fundo"
    render_template = "bannerapp/banner_plugin_1.html"
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('title'),
                ('subtitle'),
                ('b1_background_image_resize', 'background_text_alt')
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        model_name = BannerPlugin1.__name__
        resized_images = None
        background_image = None

        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name)

            background_image = {
                'desktop':resized_images[0].image_desktop.url,
                'tablet':resized_images[0].image_tablet.url,
                'mobile':resized_images[0].image_mobile.url,
            }

        context.update({
            'instance': instance,
            'background_image': background_image,
        })
        return context

#------------------------------------------------------
# 2 - Banner
#------------------------------------------------------

@plugin_pool.register_plugin
class BannerPlugin2(CMSPluginBase):
    module = 'Banner'
    model = BannerPlugin2
    form = BannerPlugin2Form
    name = "02 - Banner - Título e parágrafo para direita e imagem na esquerda"
    render_template = "bannerapp/banner_plugin_2.html"
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('title'),
                ('subtitle'),
                ('b2_left_image_resize', 'left_text_alt')
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        model_name = BannerPlugin2.__name__
        resized_images = None
        left_image = None

        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name)

            left_image = {
                'desktop':resized_images[0].image_desktop.url,
                'tablet':resized_images[0].image_tablet.url,
                'mobile':resized_images[0].image_mobile.url,
            }

        context.update({
            'instance': instance,
            'left_image': left_image,
        })
        return context

#------------------------------------------------------
# 3 - Banner
#------------------------------------------------------

@plugin_pool.register_plugin
class BannerPlugin3(CMSPluginBase):
    module = 'Banner'
    model = BannerPlugin3
    form = BannerPlugin3Form
    name = "03 - Banner - Título, subtítulo e 3 tópicos com texto e imagem"
    render_template = "bannerapp/banner_plugin_3.html"
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('title'),
                ('subtitle'),
            )
        }),
        ('Primeiro Item', {
            'fields': (
                ('first_title'),
                ('first_subtitle'),
                ('b3_first_image_resize', 'first_text_alt'),
            )
        }),
        ('Segundo Item', {
            'fields': (
                ('second_title'),
                ('second_subtitle'),
                ('b3_second_image_resize', 'second_text_alt'),
            )
        }),
        ('Terceiro Item', {
            'fields': (
                ('third_title'),
                ('third_subtitle'),
                ('b3_third_image_resize', 'third_text_alt'),
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        model_name = BannerPlugin3.__name__
        resized_images = None
        first_image = None
        second_image = None
        third_image = None

        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name)

            first_image = {
                'desktop':resized_images[0].image_desktop.url,
                'tablet':resized_images[0].image_tablet.url,
                'mobile':resized_images[0].image_mobile.url,
            }

            second_image = {
                'desktop':resized_images[1].image_desktop.url,
                'tablet':resized_images[1].image_tablet.url,
                'mobile':resized_images[1].image_mobile.url,
            }

            third_image = {
                'desktop':resized_images[2].image_desktop.url,
                'tablet':resized_images[2].image_tablet.url,
                'mobile':resized_images[2].image_mobile.url,
            }

        context.update({
            'instance': instance,
            'first_image': first_image,
            'second_image': second_image,
            'third_image': third_image,
        })
        return context
