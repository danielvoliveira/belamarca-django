from django.forms.models import ModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from djangocms_attributes_field.widgets import AttributesWidget
from djangocms_link.fields import PageSearchField

from .models import (
    FaqPlugin1,
)


# ---------------------------------------------------------
# 1 - Informações - Perguntas Frequentes
# ---------------------------------------------------------

class FaqPlugin1Form(ModelForm):

    class Meta:
        model = FaqPlugin1
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(FaqPlugin1Form, self).__init__(*args, **kwargs)
