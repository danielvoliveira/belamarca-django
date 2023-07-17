from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from genericapp.models import (
    ImagesResized,
)

from .models import (
    FormContactPlugin1,
    ContactSubject,
    FormNewsletterPlugin2,
)

from .forms import (
    FormContactPlugin1Form,
    FormNewsletterPlugin2Form,
)


# ------------------------------------------
# 01 - Contato - Formulário para contato com informações de contato
# ------------------------------------------

@plugin_pool.register_plugin
class FormContactPlugin1(CMSPluginBase):
    module = 'Formulário'
    model = FormContactPlugin1
    form = FormContactPlugin1Form
    name = '01 - Contato - Formulário para contato com informações de contato'
    render_template = "formapp/form_contact_plugin_1.html"
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('title'),
                ('subtitle'),
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        subjects = ContactSubject.objects.filter(
            disp='disponivel',
        ).order_by('name')

        context.update({
            'instance': instance,
            'subjects': subjects,
        })
        return context

@plugin_pool.register_plugin
class FormNewsletterPlugin2(CMSPluginBase):
    module = 'Formulário'
    model = FormNewsletterPlugin2
    form = FormNewsletterPlugin2Form
    name = '02 - Newsletter'
    render_template = "formapp/form_newsletter_plugin_2.html"
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                ('title'),
                ('subtitle'),
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context