from django.forms.models import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import (
    FormContactPlugin1,
    FormNewsletterPlugin2,
)

# ------------------------------------------
# 01 - Contato - Formulário para contato com informações de contato
# ------------------------------------------


class FormContactPlugin1Form(ModelForm):

    class Meta:
        model = FormContactPlugin1
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(FormContactPlugin1Form, self).__init__(*args, **kwargs)

class FormNewsletterPlugin2Form(ModelForm):

    class Meta:
        model = FormNewsletterPlugin2
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(FormNewsletterPlugin2Form, self).__init__(*args, **kwargs)