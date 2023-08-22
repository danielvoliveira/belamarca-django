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

class ColorClassesToTexts(models.TextChoices):
    ROSA_ESCURO = 'text-dark-pink-belamarca', 'Rosa Escuro'
    ROSA_CLARO = 'text-pink-belamarca', 'Rosa Claro'
    AZUL = 'text-blue-belamarca', 'Azul'
    LARANJA = 'text-orange-belamarca', 'Laranja'
    AMARELO = 'text-yellow-belamarca', 'Amarelo'
    PRETO = 'text-dark-text-belamarca', 'Preto'
    BRANCO = 'text-light-text-belamarca', 'Branco'

class FilterColorClassesToImages(models.TextChoices):
    DARK_FILTER = 'dark-filter', 'Filtro Escuro'
    WHITE_FILTER = 'withe-filter', 'Filtro Claro'

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

#------------------------------------------------------
# 4 - Banner
#------------------------------------------------------

class BannerPlugin4(CMSPlugin):

    first_title = models.CharField(
        max_length=150,
        verbose_name='Título do bloco principal',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    first_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Subtítulo do bloco princiapal',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    first_button_text = models.CharField(
        max_length=100,
        verbose_name='Texto do botão do bloco princiapal',
        default='Acesse Agora!',
        help_text='Insira o texto do botão.',
        null=False,
        blank=False,
    )

    first_button_url = models.URLField(
        verbose_name='Link para o botão do bloco princiapal',
        max_length=400,
        default='',
        null=True,
        blank=True,
    )

    b4_first_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b4_first_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 1020x880',
        on_delete=models.PROTECT
    )

    b4_first_image_size = models.CharField(
        max_length=100,
        default='1020x880',
        editable=False
    )

    first_text_alt = models.CharField(
        verbose_name='Nome da imagem do bloco principal',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    second_title = models.CharField(
        max_length=150,
        verbose_name='Título do segundo bloco',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    second_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Subtítulo do segundo bloco',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    second_button_text = models.CharField(
        max_length=100,
        verbose_name='Texto do botão do segundo bloco',
        default='Acesse Agora!',
        help_text='Insira o texto do botão.',
        null=False,
        blank=False,
    )

    second_button_url = models.URLField(
        verbose_name='Link para o botão do segundo bloco',
        max_length=400,
        default='',
        null=True,
        blank=True,
    )

    b4_second_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b4_second_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 1020x880',
        on_delete=models.PROTECT
    )

    b4_second_image_size = models.CharField(
        max_length=100,
        default='1020x880',
        editable=False
    )

    second_text_alt = models.CharField(
        verbose_name='Nome da imagem do segundo bloco',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    third_title = models.CharField(
        max_length=150,
        verbose_name='Título do terceiro bloco',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    third_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Subtítulo do terceiro bloco',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    third_button_text = models.CharField(
        max_length=100,
        verbose_name='Texto do botão do terceiro bloco',
        default='Acesse Agora!',
        help_text='Insira o texto do botão.',
        null=False,
        blank=False,
    )

    third_button_url = models.URLField(
        verbose_name='Link para o botão do terceiro bloco',
        max_length=400,
        default='',
        null=True,
        blank=True,
    )

    b4_third_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b4_third_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 1020x880',
        on_delete=models.PROTECT
    )

    b4_third_image_size = models.CharField(
        max_length=100,
        default='1020x880',
        editable=False
    )

    third_text_alt = models.CharField(
        verbose_name='Nome da imagem do terceiro bloco',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    fourth_title = models.CharField(
        max_length=150,
        verbose_name='Título do quarto bloco',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    fourth_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Subtítulo do quarto bloco',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    fourth_button_text = models.CharField(
        max_length=100,
        verbose_name='Texto do botão do quarto bloco',
        default='Acesse Agora!',
        help_text='Insira o texto do botão.',
        null=False,
        blank=False,
    )

    fourth_button_url = models.URLField(
        verbose_name='Link para o botão do quarto bloco',
        max_length=400,
        default='',
        null=True,
        blank=True,
    )

    b4_fourth_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b4_fourth_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 1020x880',
        on_delete=models.PROTECT
    )

    b4_fourth_image_size = models.CharField(
        max_length=100,
        default='1020x880',
        editable=False
    )

    fourth_text_alt = models.CharField(
        verbose_name='Nome da imagem do quarto bloco',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    fifth_title = models.CharField(
        max_length=150,
        verbose_name='Título do quinto bloco',
        default='',
        help_text='Insira o título.',
        null=False,
        blank=False,
    )

    fifth_subtitle = HTMLField(
        max_length=1500,
        verbose_name='Subtítulo do quinto bloco',
        configuration='CKEDITOR_SETTINGS',
        default='',
        null=False,
        blank=False,
    )

    fifth_button_text = models.CharField(
        max_length=100,
        verbose_name='Texto do botão do quinto bloco',
        default='Acesse Agora!',
        help_text='Insira o texto do botão.',
        null=False,
        blank=False,
    )

    fifth_button_url = models.URLField(
        verbose_name='Link para o botão do quinto bloco',
        max_length=400,
        default='',
        null=True,
        blank=True,
    )

    b4_fifth_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='b4_fifth_image_resize',
        verbose_name='Imagem a esquerda',
        help_text='Tamanho ideal 1020x880',
        on_delete=models.PROTECT
    )

    b4_fifth_image_size = models.CharField(
        max_length=100,
        default='1020x880',
        editable=False
    )

    fifth_text_alt = models.CharField(
        verbose_name='Nome da imagem do quinto bloco',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
    )

    text_color = models.CharField(
        max_length=30,
        choices=ColorClassesToTexts.choices,
        default=ColorClassesToTexts.BRANCO,
        verbose_name='Somente os textos da capa',
        help_text='Selecione a cor dos textos',
    )

    image_filter_color = models.CharField(
        max_length=30,
        choices=FilterColorClassesToImages.choices,
        default=FilterColorClassesToImages.DARK_FILTER,
        verbose_name='Usar somente a opção',
        help_text='Selecione o tipo de filtro das imagens',
    )

    def __str__(self):
        return self.first_title
