from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import (
    SeoSinglePagePlugin1,
)

from .forms import (
    SeoSinglePagePlugin1Form,
)

#------------------------------
# 1 - SEO para páginas comuns
#------------------------------

@plugin_pool.register_plugin
class SeoSinglePagePlugin1(CMSPluginBase):
    module = 'SEO'
    model = SeoSinglePagePlugin1
    form = SeoSinglePagePlugin1Form
    name = 'SEO para Redes Sociais e Google'
    render_template = "seoapp/seo_single_page_plugin_1.html"
    allow_children = False

    fieldsets = [
        ('Configuração de imagem', {
            'fields': (
                ('social_media_image'),
            )
        }),
        ('Configurações para as Redes Sociais', {
            'fields': (
                ('social_media_site_name', 'social_media_type'),
                ('social_media_title'),
                ('social_media_description'),
            )
        }),
        ('Configurações para o Google', {
            'fields': (
                ('google_name'),
                ('google_alterantive_name'),
                ('google_description'),
                ('google_logo'),
                ('google_telephone'),
                ('google_address_street'),
                ('google_address_locality', 'google_address_region'),
                ('google_social_media_facebook'),
                ('google_social_media_instagram'),
                ('google_social_media_tiktok'),
                ('google_social_media_youtube'),
            ),
        }),
    ]

    def render(self, context, instance, placeholder):
        current_url = context['request'].build_absolute_uri(context['request'].path)
        current_domain = context['request'].build_absolute_uri('/')[:-1]

        context.update({
            'instance': instance,
            'current_url': current_url,
            'current_domain': current_domain,
        })
        return context
