from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class ProductApphook(CMSApp):
    app_name = "productapp"  # must match the application namespace
    name = "Product App"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["productapp.urls"] # replace this with the path to your application's URLs module