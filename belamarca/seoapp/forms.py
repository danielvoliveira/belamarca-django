from django.forms.models import ModelForm
from django import forms

from .models import (
    SeoMetaTags,
    GoogleWebSiteMetaTag,
    GoogleCorporationMetaTag,
    GoogleProductListMetaTag,
    GoogleProductMetaTag,
)

class SeoMetaTagsForm(forms.ModelForm):
    class Meta:
        model = SeoMetaTags
        fields = '__all__'

class GoogleWebSiteMetaTagForm(forms.ModelForm):
    class Meta:
        model = GoogleWebSiteMetaTag
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