from django.forms.models import ModelForm

from .models import (
    SeoSinglePagePlugin1,
)

#------------------------------
# 1 - SEO para páginas comuns
#------------------------------

class SeoSinglePagePlugin1Form(ModelForm):

    class Meta:
        model = SeoSinglePagePlugin1
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(SeoSinglePagePlugin1Form, self).__init__(*args, **kwargs)
