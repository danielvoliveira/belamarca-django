from django.db import models
from cms.models.pluginmodel import CMSPlugin


class SocialMediaType(models.TextChoices):
    ORGANIZATION = 'organization', 'Organização/Empresa'
    WEBSITE = 'website', 'Página Web'
    BLOG = 'blog', 'Página principal do blog'

class GoogleType(models.TextChoices):
    CORPORATION = 'Corporation', 'Corporação'
    ORGANIZATION = 'Organization', 'Organização'
    PRODUCT_LIST = 'product_list', 'Lista de Produtos'
    PRODUCT = 'product', 'Página de Produto'

class ShowAddress(models.TextChoices):
    SIM = 'yes', 'Sim'
    NAO = 'no', 'Não'

#------------------------------
# 1 - SEO para páginas comuns
#------------------------------
class SeoSinglePagePlugin1(CMSPlugin):
    metadescription = models.TextField(
        verbose_name='Descrição da página para buscadores',
        max_length=250,
        default='Bela Marca: para mulheres poderosas como você.',
        help_text='Dê a cada página uma meta descrição exclusiva que reflita claramente o valor que a página carrega. Inclua suas palavras-chave mais significativas, para que elas possam ser destacadas. Mas tome cuidado para evitar o excesso de palavras-chave, não faça sua descrição apenas uma combinação de palavras-chave que você está segmentando. Limite de 250 caracteres.',
        null=True,
        blank=True,
    )

    social_media_site_name = models.CharField(
        verbose_name='Nome do site',
        max_length=100,
        default='Bela Marca',
        null=True,
        blank=True,
    )

    social_media_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=SocialMediaType.choices,
        default=SocialMediaType.WEBSITE,
    )

    social_media_title = models.CharField(
        verbose_name='Título para Redes Sociais',
        max_length=100,
        default='Bela Marca: para mulheres poderosas como você.',
        help_text='Título para ser exibido quando sua página estiver vinculada. Limite de 100 caracteres.',
        null=True,
        blank=True,
    )

    social_media_description = models.TextField(
        verbose_name='Descrição para Redes Sociais',
        max_length=300,
        default='Bela Marca: para mulheres poderosas como você.',
        help_text='Lembre-se de que o Facebook exibirá apenas cerca de 300 caracteres de descrição.',
        null=True,
        blank=True,
    )

    social_media_image = models.ImageField(
        upload_to='seo_images/',
        default='../../static/assets/seo_default_image/seo_default_image.jpg',
        null=True,
        blank=True,
        verbose_name='Imagem para Redes Sociais e Buscadores',
        help_text='Tamanho ideal 1200x630px.',
    )

    google_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=GoogleType.choices,
        default=GoogleType.CORPORATION,
        editable=False,
    )

    google_name = models.CharField(
        verbose_name='Nome do site',
        max_length=100,
        default='Bela Marca',
        null=True,
        blank=True,
    )

    google_alterantive_name = models.CharField(
        verbose_name='Nome alternativo do site',
        max_length=200,
        default='Bela Marca: para mulheres poderosas como você.',
        null=True,
        blank=True,
    )

    google_description = models.TextField(
        verbose_name='Descrição do site',
        max_length=500,
        default='Bela Marca: para mulheres poderosas como você.',
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
        max_length=100,
        default='SP',
        null=True,
        blank=True,
    )

    google_social_media_facebook = models.URLField(
        verbose_name='Link do Facebook',
        max_length=500,
        default='https://www.facebook.com/acquamotiongramado/',
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

    google_social_media_linkedin = models.URLField(
        verbose_name='Link do Linkedin',
        max_length=500,
        default='',
        null=True,
        blank=True,
    )

    google_social_media_twitter = models.URLField(
        verbose_name='Link do Twitter',
        max_length=500,
        default='',
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
        return self.social_media_title

    class Meta:
        verbose_name = "SEO para página comum"
        verbose_name_plural = "SEO para páginas comuns"

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

    social_media_site_name = models.CharField(
        verbose_name='Nome do site',
        max_length=100,
        default='Bela Marca',
        null=True,
        blank=True,
    )

    social_media_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=SocialMediaType.choices,
        default=SocialMediaType.WEBSITE,
    )

    social_media_title = models.CharField(
        verbose_name='Título para Redes Sociais',
        max_length=100,
        default='Bela Marca: para mulheres poderosas como você.',
        help_text='Título para ser exibido quando sua página estiver vinculada. Limite de 100 caracteres.',
        null=True,
        blank=True,
    )

    social_media_description = models.TextField(
        verbose_name='Descrição para Redes Sociais',
        max_length=300,
        default='Bela Marca: para mulheres poderosas como você.',
        help_text='Lembre-se de que o Facebook exibirá apenas cerca de 300 caracteres de descrição.',
        null=True,
        blank=True,
    )

    social_media_image = models.ImageField(
        upload_to='seo_images/',
        default='../../static/assets/seo_default_image/seo_default_image.jpg',
        null=True,
        blank=True,
        verbose_name='Imagem para Redes Sociais e Buscadores',
        help_text='Tamanho ideal 1200x630px.',
    )

    google_type = models.CharField(
        verbose_name='Modelo de Tags do Google a ser usado?',
        max_length=12,
        choices=GoogleType.choices,
        default=GoogleType.CORPORATION,
        editable=True,
    )

    def __str__(self):
        return self.path

    class Meta:
        verbose_name = "SEO Meta Tag"
        verbose_name_plural = "SEO Meta Tags"

class GoogleCorporationMetaTag(models.Model):
    seo_meta_tags = models.OneToOneField(
        SeoMetaTags,
        on_delete=models.CASCADE
    )

    google_type = models.CharField(
        verbose_name='Tipo de página',
        max_length=12,
        choices=GoogleType.choices,
        default=GoogleType.CORPORATION,
        editable=False,
    )

    google_name = models.CharField(
        verbose_name='Nome do site',
        max_length=100,
        default='Bela Marca',
        null=True,
        blank=True,
    )

    google_alterantive_name = models.CharField(
        verbose_name='Nome alternativo do site',
        max_length=200,
        default='Bela Marca: para mulheres poderosas como você.',
        null=True,
        blank=True,
    )

    google_description = models.TextField(
        verbose_name='Descrição do site',
        max_length=500,
        default='Bela Marca: para mulheres poderosas como você.',
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
        max_length=100,
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

    google_name = models.CharField(
        verbose_name='Nome do site',
        max_length=100,
        default='Bela Marca',
        null=True,
        blank=True,
    )

    google_alterantive_name = models.CharField(
        verbose_name='Nome alternativo do site',
        max_length=200,
        default='Bela Marca: para mulheres poderosas como você.',
        null=True,
        blank=True,
    )

    google_description = models.TextField(
        verbose_name='Descrição do site',
        max_length=500,
        default='Bela Marca: para mulheres poderosas como você.',
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
        max_length=100,
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

    google_name = models.CharField(
        verbose_name='Nome do site',
        max_length=100,
        default='Bela Marca',
        null=True,
        blank=True,
    )

    google_alterantive_name = models.CharField(
        verbose_name='Nome alternativo do site',
        max_length=200,
        default='Bela Marca: para mulheres poderosas como você.',
        null=True,
        blank=True,
    )

    google_description = models.TextField(
        verbose_name='Descrição do site',
        max_length=500,
        default='Bela Marca: para mulheres poderosas como você.',
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
        max_length=100,
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
        verbose_name = "Google Product Meta Tag"
        verbose_name_plural = "Google Product Meta Tags"