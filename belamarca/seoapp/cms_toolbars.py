from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from seoapp.models import SeoMetaTags


@toolbar_pool.register  # register the toolbar
class SeoToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            key='seo_toolbar',
            verbose_name='Seo'
        )

        path = self.request.environ['PATH_INFO']
        current_seo = SeoMetaTags.objects.filter(path=path)

        if len(current_seo) > 0:
            menu.add_sideframe_item(
                name='Editar Seo desta página',
                url='/admin/seoapp/seometatags/{}/change/'.format(current_seo[0].id)
            )

        #menu.add_sideframe_item(
        #    name='Lista de Seo',
        #    url=admin_reverse('seoapp_seometatags_changelist')
        #)
