#------------------------------------------#
#------------------------------------------#
# Suporte para plugins com links externos
# ou internos
#------------------------------------------#
#------------------------------------------#

from djangocms_link import models as djangocms_link
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def get_link(instance):
    '''
    Função usada na criação do CMS Plugin (cms_plugin.py) para
    retornar link atual da instancia recebida. Precisamos ter
    no modelo do plugin os fields: 'internal_link' e
    'external_link' criados e configurados.
    '''
    if instance.internal_link:
        ref_page = instance.internal_link
        link = ref_page.get_absolute_url()

        # simulate the call to the unauthorized CMSPlugin.page property
        cms_page = instance.placeholder.page if instance.placeholder_id else None

        # first, we check if the placeholder the plugin is attached to
        # has a page. Thus the check "is not None":
        if cms_page is not None:
            if getattr(cms_page, 'node', None):
                cms_page_site_id = getattr(cms_page.node, 'site_id', None)
            else:
                cms_page_site_id = getattr(cms_page, 'site_id', None)
        # a plugin might not be attached to a page and thus has no site
        # associated with it. This also applies to plugins inside
        # static placeholders
        else:
            cms_page_site_id = None

        # now we do the same for the reference page the plugin links to
        # in order to compare them later
        if cms_page is not None:
            if getattr(cms_page, 'node', None):
                ref_page_site_id = ref_page.node.site_id
            else:
                ref_page_site_id = ref_page.site_id
        # if no external reference is found the plugin links to the
        # current page
        else:
            ref_page_site_id = djangocms_link.Site.objects.get_current().pk

        if ref_page_site_id != cms_page_site_id:
            ref_site = djangocms_link.Site.objects._get_site_by_id(ref_page_site_id).domain
            link = '//{}{}'.format(ref_site, link)

    elif instance.external_link:
        link = instance.external_link

    else:
        link = ''

    return link

def get_form(super, obj, self, request, **kwargs):
    '''
    Função usada na criação do formulário do CMS Plugin (cms_plugin.py)
    para retornar o form_class e o site ('django.contrib.sites.models.Site')
    dos parametros recebidos enviados pelo plugin. Para esse retorno,
    precisamos receber o self do plugin e o obj dentro da função
    'get_form' do respectivo plugin.
    '''
    form_class = super.get_form(request, obj, **kwargs)
    site = None
    if obj and obj.page and hasattr(obj.page, 'site') and obj.page.site:
        site = obj.page.site
    elif self.page and hasattr(self.page, 'site') and self.page.site:
        site = self.page.site
    else:
        site = Site.objects.get_current()

    return {
        'form_class':form_class,
        'site':site,
    }

def clean(super, self):
    '''
    Esta função é chamada diretamente no modelo, que deve ter os atributos
    'url_validators', 'external_link' e 'internal_link', para verificar
    se o campo de link foi preenchido, retornando algumas exceções
    em certos casos:
    - Quando nenhum dos campos é preenchido
    - Quando o link externo é inválido
    - Quando os dois são preenchidos simultaneamente
    '''
    super.clean()
    field_names = (
        'external_link',
        'internal_link',
    )

    link_fields = {
        key: getattr(self, key)
        for key in field_names
    }
    link_field_verbose_names = {
        key: djangocms_link.force_text(self._meta.get_field(key).verbose_name)
        for key in link_fields.keys()
    }
    provided_link_fields = {
        key: value
        for key, value in link_fields.items()
        if value
    }

    if len(provided_link_fields) > 1:
        # Too many fields have a value.
        verbose_names = sorted(link_field_verbose_names.values())
        error_msg = _('Only one of {0} or {1} may be given.').format(
            ', '.join(verbose_names[:-1]),
            verbose_names[-1],
        )
        errors = {}.fromkeys(provided_link_fields.keys(), error_msg)
        raise ValidationError(errors)

    if (len(provided_link_fields) == 0):
        raise ValidationError(
            _('Please provide a link.')
        )

def for_site(site, self):
    # override the internal_link fields queryset to contains just pages for
    # current site
    # this will work for PageSelectFormField
    from cms.models import Page
    self.fields['internal_link'].queryset = Page.objects.drafts().on_site(site)
    # set the current site as a internal_link field instance attribute
    # this will be used by the field later to properly set up the queryset
    # this will work for PageSearchField
    self.fields['internal_link'].site = site
    self.fields['internal_link'].widget.site = site