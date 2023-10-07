from django.db import models
from cms.models.pluginmodel import CMSPlugin


class SocialMediaType(models.TextChoices):
    ORGANIZATION = 'organization', 'Organização/Empresa'
    WEBSITE = 'website', 'Página Web'
    BLOG = 'blog', 'Página principal do blog'

class GoogleType(models.TextChoices):
    WEBSITE = 'WebSite', 'Página do Web Site'
    ORGANIZATION = 'Organization', 'Organização'
    PRODUCT_LIST = 'ItemList', 'Lista de Produtos'
    PRODUCT = 'Product', 'Página de Produto'

class ShowAddress(models.TextChoices):
    SIM = 'yes', 'Sim'
    NAO = 'no', 'Não'

#------------------------------
# SEO para páginas comuns
#------------------------------

class SeoMetaTags(models.Model):
    path = models.CharField(
        verbose_name='Path da página',
        max_length=300,
        null=True,
        blank=True,
        editable=False,
    )

    title = models.CharField(
        verbose_name='Título da página para SEO',
        max_length=250,
        default='Bela Marca: a sua marca de moda praia',
        help_text='Dê a cada página um meta título exclusivo que reflita claramente o valor que a página carrega. Limite de 60 caracteres.',
        null=True,
        blank=True,
    )

    description = models.TextField(
        verbose_name='Descrição da página para SEO',
        max_length=250,
        default='Conheça nossa nova coleção 2024. Seja uma parceira da marca mais completa e estilosa de moda praia. Seus clientes merecem. Venha espalhar Bela Marca por aí!',
        help_text='Dê a cada página uma meta descrição exclusiva que reflita claramente o valor que a página carrega. Inclua suas palavras-chave mais significativas, para que elas possam ser destacadas. Mas tome cuidado para evitar o excesso de palavras-chave, não faça sua descrição apenas uma combinação de palavras-chave que você está segmentando. Limite de 250 caracteres.',
        null=True,
        blank=True,
    )

    site_name = models.CharField(
        verbose_name='Nome do site para SEO',
        max_length=100,
        default='Bela Marca',
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='seo_images/',
        default='../../static/assets/seo_default_image/seo_default_image.jpg',
        null=True,
        blank=True,
        verbose_name='Imagem para SEO',
        help_text='Tamanho ideal 1200x630px.',
    )

    social_media_type = models.CharField(
        verbose_name='Tipo de página para Instagram e Facebook',
        max_length=12,
        choices=SocialMediaType.choices,
        default=SocialMediaType.WEBSITE,
        editable=False,
    )

    def __str__(self):
        return self.path

    class Meta:
        verbose_name = "SEO Meta Tag"
        verbose_name_plural = "SEO Meta Tags"

class GoogleWebSiteMetaTag(models.Model):
    seo_meta_tags = models.OneToOneField(
        SeoMetaTags,
        on_delete=models.CASCADE
    )

    google_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=GoogleType.choices,
        default=GoogleType.WEBSITE,
        editable=False,
    )

    def __str__(self):
        return self.google_type

    class Meta:
        verbose_name = "Google Web Site Meta Tag"
        verbose_name_plural = "Google Web Site Meta Tags"

class GoogleCorporationMetaTag(models.Model):
    seo_meta_tags = models.OneToOneField(
        SeoMetaTags,
        on_delete=models.CASCADE
    )

    google_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=GoogleType.choices,
        default=GoogleType.ORGANIZATION,
        editable=False,
    )

    google_alterantive_name = models.CharField(
        verbose_name='Nome alternativo do site',
        max_length=200,
        default='Bela Marca - Beach Wear.',
        null=True,
        blank=True,
    )

    google_logo = models.ImageField(
        upload_to='seo_images/',
        default='../../static/assets/logo/logo_quadrado_turquesa.png',
    )

    google_telephone = models.CharField(
        verbose_name='Telefone para contato',
        max_length=20,
        default='5513997977005',
        null=True,
        blank=True,
    )

    google_address_type = models.CharField(
        verbose_name='Tipo de endereço',
        max_length=40,
        default='postalAddress',
        null=True,
        blank=True,
        editable=False,
    )

    google_address_street = models.CharField(
        verbose_name='Endereço',
        max_length=200,
        default='',
        null=True,
        blank=True,
    )

    google_address_locality = models.CharField(
        verbose_name='Cidade',
        max_length=100,
        default='Praia Grande',
        null=True,
        blank=True,
    )

    google_address_region = models.CharField(
        verbose_name='Estado',
        max_length=2,
        default='SP',
        null=True,
        blank=True,
    )

    google_social_media_facebook = models.URLField(
        verbose_name='Link do Facebook',
        max_length=500,
        default='',
        null=True,
        blank=True,
    )

    google_social_media_instagram = models.URLField(
        verbose_name='Link do Instagram',
        max_length=500,
        default='https://www.instagram.com/belamarcastore/',
        null=True,
        blank=True,
    )

    google_social_media_youtube = models.URLField(
        verbose_name='Link do Youtube',
        max_length=500,
        default='',
        null=True,
        blank=True,
    )

    google_social_media_tiktok = models.URLField(
        verbose_name='Link do TikTok',
        max_length=500,
        default='',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.google_type

    class Meta:
        verbose_name = "Google Corporation Meta Tag"
        verbose_name_plural = "Google Corporation Meta Tags"

class GoogleProductListMetaTag(models.Model):
    seo_meta_tags = models.OneToOneField(
        SeoMetaTags,
        on_delete=models.CASCADE
    )

    google_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=GoogleType.choices,
        default=GoogleType.PRODUCT_LIST,
        editable=False,
    )

    def __str__(self):
        return self.google_type

    class Meta:
        verbose_name = "Google Product List Meta Tag"
        verbose_name_plural = "Google Product List Meta Tags"

class GoogleProductMetaTag(models.Model):
    seo_meta_tags = models.OneToOneField(
        SeoMetaTags,
        on_delete=models.CASCADE
    )

    google_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=GoogleType.choices,
        default=GoogleType.PRODUCT,
        editable=False,
    )

    google_product_code = models.CharField(
        verbose_name='Código do Produto',
        max_length=100,
        default='',
        null=True,
        blank=True,
    )

    google_product_name = models.CharField(
        verbose_name='Nome do Produto',
        max_length=200,
        default='',
        null=True,
        blank=True,
    )

    google_product_description = models.TextField(
        verbose_name='Descrição do Produto',
        max_length=300,
        default='',
        null=True,
        blank=True,
    )

    google_product_price = models.CharField(
        verbose_name='Preço do Produto',
        max_length=12,
        help_text='Inserir somente o valor no seguinte formato "100.00".',
        default='',
        null=True,
        blank=True,
    )

    google_product_image = models.ImageField(
        upload_to='seo_images/',
        default='../../static/assets/logo/logo_quadrado_turquesa.png',
    )

    def __str__(self):
        return self.google_type

    class Meta:
        verbose_name = "Google Product Meta Tag"
        verbose_name_plural = "Google Product Meta Tags"