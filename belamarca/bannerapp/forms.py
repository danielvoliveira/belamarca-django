from django.forms.models import ModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _

from djangocms_attributes_field.widgets import AttributesWidget
from djangocms_link.fields import PageSearchField

from .models import (
    BannerPlugin1,
    BannerPlugin2,
    BannerPlugin3,
)

#------------------------------------------------------
# 1 - Página Inicial - Título e parágrafo
#------------------------------------------------------

class BannerPlugin1Form(ModelForm):

    class Meta:
        model = BannerPlugin1
        exclude = ('b1_background_image_size',)

    def __init__(self, *args, **kwargs):
        super(BannerPlugin1Form, self).__init__(*args, **kwargs)


#------------------------------------------------------
# 2 - Banner
#------------------------------------------------------

class BannerPlugin2Form(ModelForm):

    class Meta:
        model = BannerPlugin2
        exclude = ('b2_left_image_size',)

    def __init__(self, *args, **kwargs):
        super(BannerPlugin2Form, self).__init__(*args, **kwargs)

#------------------------------------------------------
# 3 - Banner
#------------------------------------------------------

class BannerPlugin3Form(ModelForm):

    class Meta:
        model = BannerPlugin3
        exclude = ('b3_first_image_size', 'b3_second_image_size', 'b3_third_image_size')

    def __init__(self, *args, **kwargs):
        super(BannerPlugin3Form, self).__init__(*args, **kwargs)

