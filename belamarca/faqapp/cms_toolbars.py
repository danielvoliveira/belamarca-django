from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import SubMenu

from cms.utils.urlutils import admin_reverse


@toolbar_pool.register  # register the toolbar
class CarouselToolbar(CMSToolbar):

    def populate(self):
        menu_carousel = self.toolbar.get_or_create_menu(
            'faq',  # a unique key for this menu
            'Faq',  # the text that should appear in the menu
        )

        menu_carousel.add_sideframe_item(
            name='Lista de perguntas e respostas',  # name of the new menu item
            # the URL it should open with
            url=admin_reverse('faqapp_detailfaqplugin1_changelist'),
        )

        menu_carousel.add_modal_item(
            name='Cadastrar nova pergunta',
            url=admin_reverse('faqapp_detailfaqplugin1_add'),
        )
