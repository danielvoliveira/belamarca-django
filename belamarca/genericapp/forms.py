from django.forms.models import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import (
    GenericHeaderPlugin1,
    GenericFooterPlugin2,
    GenericIconsPlugin3,
)

# ----------------------------------------
# 1 - Cabeçalho - Logo, menu com submenu e botão
# ----------------------------------------


class GenericHeaderPlugin1Form(ModelForm):

    class Meta:
        model = GenericHeaderPlugin1
        exclude = ('g1_logo_image_size',)

    def __init__(self, *args, **kwargs):
        super(GenericHeaderPlugin1Form, self).__init__(*args, **kwargs)


# ------------------------------------------------------------
# 2 - Rodapé - Logo, redes sociais, links úteis e assinatura
# ------------------------------------------------------------

class GenericFooterPlugin2Form(ModelForm):

    class Meta:
        model = GenericFooterPlugin2
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(GenericFooterPlugin2Form, self).__init__(*args, **kwargs)

# ------------------------------------------------------------
# 3 - Ícones Flutuantes - Voltar ao topo e whatsapp
# ------------------------------------------------------------


class GenericIconsPlugin3Form(ModelForm):

    class Meta:
        model = GenericIconsPlugin3
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(GenericIconsPlugin3Form, self).__init__(*args, **kwargs)
