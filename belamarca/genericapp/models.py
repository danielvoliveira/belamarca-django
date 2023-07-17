from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField


# ----------------------------------------
# 1 - Cabeçalho - Logo, menu com submenu e botão
# ----------------------------------------

class GenericHeaderPlugin1(CMSPlugin):
    g1_logo_image_resize = FilerImageField(
        null=False,
        blank=False,
        related_name='g1_logo_image_resize',
        verbose_name='Imagem da logo Ex.: Logo Branca.',
        help_text='Tamanho ideal 205x177.',
        on_delete=models.PROTECT
    )

    g1_logo_image_size = models.CharField(
        max_length=100,
        default='205x177',
        editable=False,
    )

    text_alt = models.CharField(
        verbose_name='Nome da imagem',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
        default='',
    )

# ------------------------------------------------------------
# 2 - Rodapé - Logo, redes sociais, links úteis e assinatura
# ------------------------------------------------------------


class GenericFooterPlugin2(CMSPlugin):
    g2_logo_image_resize = FilerImageField(
        null=False,
        blank=False,
        related_name='g2_logo_image_resize',
        verbose_name='Imagem da logo.',
        help_text='Tamanho ideal 205x177.',
        on_delete=models.PROTECT
    )

    g2_logo_image_size = models.CharField(
        max_length=100,
        default='205x177',
        editable=False,
    )

    text_alt = models.CharField(
        verbose_name='Nome da imagem',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
        default='Logo do Bela Marca',
    )

    text_address = HTMLField(
        verbose_name='Endereço completo',
        max_length=200,
        help_text='Digite o endereço com rua, numero, bairro e cep.',
        null=False,
        blank=False,
        default='<p>Estrada Municipal Linha Ávila,<br>Rua Linha Carazal, 501<br>Gramado/RS - 95670-000</p>',
    )

    text_phone = models.CharField(
        verbose_name='Numero de telefone',
        max_length=100,
        help_text='Digite numero de telefone para contato.',
        null=False,
        blank=False,
        default='+55 54 3050-1700',
    )

    text_email = models.CharField(
        verbose_name='E-mail',
        max_length=100,
        help_text='Digite o endereço de e-mail para contato.',
        null=False,
        blank=False,
        default='acquamotion@gramadoparks.com',
    )

    text_hours = HTMLField(
        verbose_name='Horário de funcionamento',
        max_length=100,
        help_text='Digite qual será o texto para indicar o horário de funcionamento. Ex.: Aberto das 09h ás 17h',
        null=False,
        blank=False,
        default='das 10h às 18h<br>Consulte dias de abertura',
    )

    url_instagram = models.URLField(
        verbose_name='Link para o Instagram',
        max_length=300,
        default='',
        null=True,
        blank=True,
    )

    text_alt_instagram = models.CharField(
        verbose_name='Nome da imagem',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
        default='Ícone do Instagram',
        editable=False,
    )

    url_facebook = models.URLField(
        verbose_name='Link para o Facebook',
        max_length=300,
        default='',
        null=True,
        blank=True,
    )

    text_alt_facebook = models.CharField(
        verbose_name='Nome da imagem',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
        default='Ícone do Facebook',
        editable=False,
    )

    url_tiktok = models.URLField(
        verbose_name='Link para o TikTok',
        max_length=300,
        default='',
        null=True,
        blank=True,
    )

    text_alt_tiktok = models.CharField(
        verbose_name='Nome da imagem',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
        default='Ícone do TikTok',
        editable=False,
    )

    url_youtube = models.URLField(
        verbose_name='Link do Youtube',
        max_length=300,
        default='',
        null=True,
        blank=True,
    )

    text_alt_youtube = models.CharField(
        verbose_name='Nome da imagem',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
        default='Ícone do Youtube',
        editable=False,
    )

# ------------------------------------------------------------
# 3 - Ícones Flutuantes - Voltar ao topo e whatsapp
# ------------------------------------------------------------


class GenericIconsPlugin3(CMSPlugin):
    g3_whatsapp_image_resize = FilerImageField(
        null=False,
        blank=False,
        related_name='g3_whats_image_resize',
        verbose_name='Logo do WhatsApp',
        help_text='Tamanho ideal 50x50.',
        on_delete=models.PROTECT
    )

    g3_whatsapp_image_size = models.CharField(
        max_length=100,
        default='50x50',
        editable=False,
    )

    text_alt = models.CharField(
        verbose_name='Nome da imagem',
        max_length=100,
        help_text='Digite o nome descritivo para a imagem.',
        null=False,
        blank=False,
        default='Ícone do WhatsApp',
    )

    whatsapp_number = models.CharField(
        verbose_name='Número do Whatsapp',
        max_length=13,
        help_text='Inclua somente os números (ex: 5517999999999)',
        default='5513997977005',
        null=False,
        blank=False,
    )

# ------------------------------------------------------------
# 4 - Política e Privacidade - Título e texto
# ------------------------------------------------------------


class GenericPrivacyPolicyPlugin4(models.Model):

    title = models.CharField(
        max_length=100,
        default=_('Política de Privacidade'),
        verbose_name='Título',
        null=False,
        blank=False,
    )

    text = HTMLField(
        null=False,
        blank=False,
        verbose_name='Texto',
        configuration='CKEDITOR_SETTINGS',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Política de Privacidade"
        verbose_name_plural = "Políticas de Privacidade"


# ------------------------------------------------------------
# 5 - Termos e Condições - Título subtítulo e texto
# ------------------------------------------------------------


class GenericTermsAndConditionsPlugin5(models.Model):
    '''
    5 - Termos e Condições - Título subtítulo e texto
    '''
    title = models.CharField(
        max_length=1000,
        default=_('Termos e Condições'),
        verbose_name='Título',
        null=False,
        blank=False,
    )

    text = HTMLField(
        null=False,
        blank=False,
        verbose_name='Texto',
        configuration='CKEDITOR_SETTINGS',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Termo e Condição"
        verbose_name_plural = "Termos e Condições"


# ------------------------------------------
# 06 - Newsletter - Nome, e-mail e termos
# ------------------------------------------


class NewsLetter(models.Model):
    nome = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        max_length=100
    )

    termos = models.BooleanField(
        default=False
    )

    def __str__(self):
        return '{} ({})'.format(self.nome, self.email)

    class Meta:
        verbose_name = "Cadastro da Newsletter"
        verbose_name_plural = "Cadastros das Newsletter"


# ------------------------------------------
# 07 - Política de Reagendamento, Cancelamento e No-Show - Título e texto
# ------------------------------------------


class GenericNoShowPlugin7(models.Model):
    '''
    7 - Política e Privacidade - Título e texto
    '''
    title = models.CharField(
        max_length=1000,
        default=_('Política de Reagendamento, Cancelamento e No-Show'),
        verbose_name='Título',
        null=False,
        blank=False,
    )

    text = HTMLField(
        null=False,
        blank=False,
        verbose_name='Texto',
        configuration='CKEDITOR_SETTINGS',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Política de Reagendamento, Cancelamento e No-Show"
        verbose_name_plural = "Política de Reagendamento, Cancelamento e No-Show"


# ------------------------------------------------------
# Modelo para armazenamento das imagens redimensionadas
# ------------------------------------------------------


class ImagesResized(models.Model):
    image_mobile = models.ImageField(
        verbose_name='Imagem mobile', help_text='Gerada Automáticamente.', max_length=400, blank=True)
    image_tablet = models.ImageField(
        verbose_name='Imagem tablet', help_text='Gerada Automáticamente.', max_length=400, blank=True)
    image_desktop = models.ImageField(
        verbose_name='Imagem desktop', help_text='Gerada Automáticamente.', max_length=400, blank=True)
    model_name = models.CharField(max_length=150, default='Model Name')
    model_id = models.BigIntegerField(blank=True, null=True)
    field_name = models.CharField(max_length=150, default='Field Name')

    def __str__(self):
        return str(self.id)
