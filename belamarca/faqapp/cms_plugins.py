from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import (
    FaqPlugin1,
    DetailFaqPlugin1,
)

from .forms import (
    FaqPlugin1Form,
)

# ----------------------------------------
# 1 - Informações - Perguntas Frequentes
# ----------------------------------------

@plugin_pool.register_plugin
class FaqPlugin1(CMSPluginBase):
    module = 'Faq'
    model = FaqPlugin1
    form = FaqPlugin1Form
    name = "01 - Faq - Informações - Perguntas Frequentes"
    render_template = 'faqapp/faq_plugin_1.html'
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('title'),
                ('ordination'),
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        ordination = instance.ordination
        if ordination == 'new_to_old':
            ordination = '-id'
        elif ordination == 'old_to_new':
            ordination = 'id'
        elif ordination == 'random':
            ordination = '?'

        context['questions'] = DetailFaqPlugin1.objects.filter(
            disp='disponivel',
        ).order_by(ordination)

        title_colors = [
            'dark-pink-text',
            'pink-text',
            'orange-text',
            #'blue-text',
        ]

        color_position = 0
        number = 1
        for i, item in enumerate(context['questions']):
            item.number = number
            item.title_color = title_colors[color_position]
            color_position += 1
            number += 1

            if (len(title_colors) - 1) < color_position:
                color_position = 0

        context.update({
            'instance': instance,
        })
        return context
