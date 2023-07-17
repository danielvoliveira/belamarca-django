from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.core.exceptions import ValidationError
from djangocms_link.validators import IntranetURLValidator
from django.utils.translation import gettext_lazy as _
from djangocms_attributes_field.fields import AttributesField
from djangocms_link import models as djangocms_link
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from mainsite.utils.external_and_internal_link import (
    clean,
)

#------------------------------------------------------
# 1 - Banner
#------------------------------------------------------

class BannerPlugin1(CMSPlugin):
    b1_background_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b1_background_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 1650x400',
        on_delete=models.PROTECT
    )

    b1_background_image_size = models.CharField(
        max_length=100,
        default='1650x400',
        editable=False
    )

    background_text_alt = models.CharField(
        verbose_name='Nome da imagem a esquerda',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Título a direita',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    subtitle = HTMLField(
        max_length=1500,
        verbose_name='Descrição a direita',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

#------------------------------------------------------
# 2 - Banner
#------------------------------------------------------

class BannerPlugin2(CMSPlugin):
    b2_left_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b2_left_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 540x400',
        on_delete=models.PROTECT
    )

    b2_left_image_size = models.CharField(
        max_length=100,
        default='540x400',
        editable=False
    )

    left_text_alt = models.CharField(
        verbose_name='Nome da imagem a esquerda',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Título a direita',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    subtitle = HTMLField(
        max_length=1500,
        verbose_name='Descrição a direita',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

#------------------------------------------------------
# 3 - Banner
#------------------------------------------------------

class BannerPlugin3(CMSPlugin):

    title = models.CharField(
        max_length=150,
        verbose_name='Título',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    subtitle = HTMLField(
        max_length=1500,
        verbose_name='Descrição',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    first_title = models.CharField(
        max_length=150,
        verbose_name='Primeiro título',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    first_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Primeira descrição',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    b3_first_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b3_first_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 630x508',
        on_delete=models.PROTECT
    )

    b3_first_image_size = models.CharField(
        max_length=100,
        default='630x508',
        editable=False
    )

    first_text_alt = models.CharField(
        verbose_name='Nome da imagem a esquerda',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    second_title = models.CharField(
        max_length=150,
        verbose_name='Segundo título',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    second_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Segunda descrição',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    b3_second_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b3_second_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 630x508',
        on_delete=models.PROTECT
    )

    b3_second_image_size = models.CharField(
        max_length=100,
        default='630x508',
        editable=False
    )

    second_text_alt = models.CharField(
        verbose_name='Nome da imagem a esquerda',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    third_title = models.CharField(
        max_length=150,
        verbose_name='Terceiro título',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    third_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Terceira descrição',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    b3_third_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b3_left_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 630x508',
        on_delete=models.PROTECT
    )

    b3_third_image_size = models.CharField(
        max_length=100,
        default='630x508',
        editable=False
    )

    third_text_alt = models.CharField(
        verbose_name='Nome da imagem a esquerda',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title
