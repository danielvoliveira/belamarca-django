from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import (
    ImagesResized,
    GenericHeaderPlugin1,
    GenericFooterPlugin2,
    GenericIconsPlugin3,
)

from .forms import (
    GenericHeaderPlugin1Form,
    GenericFooterPlugin2Form,
    GenericIconsPlugin3Form,
)


# ----------------------------------------
# 1 - Cabeçalho - Logo, menu com submenu e botão
# ----------------------------------------

@plugin_pool.register_plugin
class GenericHeaderPlugin1(CMSPluginBase):
    module = 'Genérico'
    model = GenericHeaderPlugin1
    # form = GenericHeaderPlugin1Form
    name = '01 - Cabeçalho - Logo, menu com submenu e botão'
    render_template = "genericapp/generic_header_plugin_1.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        model_name = GenericHeaderPlugin1.__name__
        resized_images = None
        logo_image = None

        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name)
            logo_image = {
                'desktop': resized_images[0].image_desktop.url,
                'tablet': resized_images[0].image_tablet.url,
                'mobile': resized_images[0].image_mobile.url,
            }
        context.update({
            'instance': instance,
            'logo_image': logo_image,
        })
        return context

# ------------------------------------------------------------
# 2 - Rodapé - Logo, dados, redes sociais, links úteis e formulário
# ------------------------------------------------------------


@plugin_pool.register_plugin
class GenericFooterPlugin2(CMSPluginBase):
    module = 'Genérico'
    model = GenericFooterPlugin2
    form = GenericFooterPlugin2Form
    name = '02 - Rodapé - Logo, dados, redes sociais, links úteis e formulário'
    render_template = "genericapp/generic_footer_plugin_2.html"
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('g2_logo_image_resize', 'text_alt'),
                # ('assinatura'),
            )
        }),
        ('Informações', {
            'classes': ('collapse',),
            'fields': (
                ('text_address'),
                ('text_phone'),
                ('text_email'),
                ('text_hours'),
            ),
        }),
        ('Redes Sociais', {
            'classes': ('collapse',),
            'fields': (
                ('url_instagram'),
                ('url_facebook'),
                ('url_tiktok'),
                ('url_youtube'),
            ),
        }),
    ]

    def render(self, context, instance, placeholder):
        model_name = GenericFooterPlugin2.__name__
        resized_images = None
        logo_image = None

        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name)

            logo_image = {
                'desktop': resized_images[0].image_desktop.url,
                'tablet': resized_images[0].image_tablet.url,
                'mobile': resized_images[0].image_mobile.url,
            }

        context.update({
            'instance': instance,
            'logo_image': logo_image,
        })
        return context

# ------------------------------------------------------------
# 3 - Ícones Flutuantes - Voltar ao topo e whatsapp
# ------------------------------------------------------------


@plugin_pool.register_plugin
class GenericIconsPlugin3(CMSPluginBase):
    module = 'Genérico'
    model = GenericIconsPlugin3
    form = GenericIconsPlugin3Form
    name = '03 - Ícones Flutuantes - Voltar ao topo e whatsapp'
    render_template = "genericapp/generic_icons_plugin_3.html"
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('g3_whatsapp_image_resize', 'text_alt'),
                ('whatsapp_number'),
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        model_name = GenericIconsPlugin3.__name__
        resized_images = None
        logo_image = None

        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name)

            logo_image = {
                'desktop': resized_images[0].image_desktop.url,
                'tablet': resized_images[0].image_tablet.url,
                'mobile': resized_images[0].image_mobile.url,
            }

        context.update({
            'instance': instance,
            'logo_image': logo_image,
        })
        return context


# ----------------------------------------
# 1 - Home Index
# ----------------------------------------

@plugin_pool.register_plugin
class GenericStaticHome(CMSPluginBase):
    module = 'Genérico'
    # form = GenericHeaderPlugin1Form
    name = '01 - Static Home'
    render_template = "genericapp/generic_static_home.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context