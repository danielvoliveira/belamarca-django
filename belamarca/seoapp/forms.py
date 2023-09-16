from django.forms.models import ModelForm
from django import forms

from .models import (
    SeoSinglePagePlugin1,
    SeoMetaTags,
    GoogleCorporationMetaTag,
    GoogleProductListMetaTag,
    GoogleProductMetaTag,
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

class SeoMetaTagsForm(forms.ModelForm):
    class Meta:
        model = SeoMetaTags
        fields = '__all__'

class GoogleCorporationMetaTagForm(forms.ModelForm):
    class Meta:
        model = GoogleCorporationMetaTag
        fields = '__all__'

class GoogleProductListMetaTagForm(forms.ModelForm):
    class Meta:
        model = GoogleProductListMetaTag
        fields = '__all__'

class GoogleProductMetaTagForm(forms.ModelForm):
    class Meta:
        model = GoogleProductMetaTag
        fields = '__all__'