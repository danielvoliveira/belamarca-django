from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import SubMenu
from cms.utils.urlutils import admin_reverse


#@toolbar_pool.register  # register the toolbar
#class FormsToolbar(CMSToolbar):
#    def populate(self):
#        menu_form = self.toolbar.get_or_create_menu(
#            'formapp',  # a unique key for this menu
#            'Formulários',  # the text that should appear in the menu
#        )
#        position = menu_form.get_alphabetical_insert_position(
#            'Formularios',
#            SubMenu
#        )

#        newsletter = menu_form.get_or_create_menu(
#            'newsletter-menu',
#            'Newsletter',
#            position=position
#        )
#        newsletter.add_sideframe_item(
#            name='Lista de assinantes',  # name of the new menu item
#            # the URL it should open with
#            url=admin_reverse('formapp_newsletter_changelist'),
#        )