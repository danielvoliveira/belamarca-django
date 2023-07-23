from email.policy import default
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify


class Disponibility(models.TextChoices):
    DISPONIVEL = 'disponivel', 'Disponível'
    INDISPONIVEL = 'indisponivel', 'Indisponível'

# ------------------------------------------
# 01 - Categorias
# ------------------------------------------

class Category(models.Model):
    name = models.CharField(
        verbose_name='Nome da categoria',
        max_length=120,
        null=False,
        blank=False,
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
    )

    # title = models.CharField(
    #     verbose_name='Título da categoria',
    #     max_length=200,
    #     help_text='Máximo de 200 catacteres.',
    #     null=True,
    #     blank=True,
    #     default='Título',
    # )

    # subtitle = models.CharField(
    #     verbose_name='Subtítulo da categoria',
    #     max_length=300,
    #     help_text='Máximo de 300 catacteres.',
    #     null=True,
    #     blank=True,
    #     default='Subtítulo',
    # )

    # url = models.URLField(
    #     verbose_name='Link da categoria',
    #     max_length=300,
    #     default='',
    #     null=True,
    #     blank=True,
    # )

    # category_image_resize = FilerImageField(
    #     null=True,
    #     blank=True,
    #     related_name='g2_logo_image_resize',
    #     verbose_name='Imagem da categoria',
    #     help_text='Tamanho ideal 543x465.',
    #     on_delete=models.PROTECT
    # )

    # category_image_size = models.CharField(
    #     max_length=100,
    #     default='543x465',
    #     editable=False,
    # )

    # text_alt = models.CharField(
    #     verbose_name='Texto alternativo da imagem',
    #     max_length=100,
    #     help_text='Digite o nome descritivo para a imagem.',
    #     null=True,
    #     blank=True,
    #     default='Imagem da Categoria',
    # )

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']


class Subcategory(models.Model):
    name = models.CharField(
        verbose_name='Nome da subcategoria',
        max_length=120,
        null=False,
        blank=False,
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
    )

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['name']

# ------------------------------------------
# 02 - Atributos
# ------------------------------------------

class Attribute(models.Model):
    name = models.CharField(
        verbose_name='Nome do atributo',
        max_length=120,
        null=False,
        blank=False,
    )

    is_text = models.BooleanField(
        default=False
    )

    is_image = models.BooleanField(
        default=False
    )

    is_color = models.BooleanField(
        default=False
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
    )

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'
        ordering = ['id']


class AttributeOption(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.PROTECT,
    )

    name = models.CharField(
        verbose_name='Nome do atributo',
        max_length=120,
        null=False,
        blank=False,
        default=''
    )

    text = models.CharField(
        verbose_name='Texto do atributo',
        max_length=120,
        null=True,
        blank=True,
    )

    p2_image_image_resize = FilerImageField(
        null=True,
        blank=True,
        related_name='p2_image_image_resize',
        verbose_name='Imagem do atributo.',
        help_text='Tamanho ideal 100x100.',
        on_delete=models.PROTECT
    )

    p2_image_image_size = models.CharField(
        max_length=100,
        default='100x100',
        editable=False,
    )

    color = models.CharField(
        verbose_name='Hexadecimal da cor',
        max_length=7,
        null=True,
        blank=True,
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
    )

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.attribute, self.name)

    class Meta:
        verbose_name = 'Opção de Atributo'
        verbose_name_plural = 'Opções de Atributos'


# ------------------------------------------
# 03 - Produtos
# ------------------------------------------

class Product(models.Model):
    code = models.CharField(
        verbose_name='Código do produto',
        max_length=100,
        null=False,
        blank=False,
    )

    name = models.CharField(
        verbose_name='Nome do produto',
        max_length=150,
        null=False,
        blank=False,
    )

    description = HTMLField(
        verbose_name='Descrição',
        max_length=1000,
        help_text='Digite a descrições do produto',
        null=True,
        blank=True,
        default='',
    )

    datasheet = HTMLField(
        verbose_name='Ficha Técnica',
        max_length=1000,
        help_text='Digite as específicações do produto',
        null=True,
        blank=True,
        default='',
    )

    slug = models.SlugField(
        verbose_name='Slug do produto',
        max_length=300,
        null=False,
        blank=True,
        unique=True,
        default='',
    )

    def allCategories():
        categories_list = Category.objects.all()
        if categories_list:
            return categories_list[0].id
        else:
            return None

    category = models.ManyToManyField(
        Category,
        verbose_name='Categorias',
    )

    def allSubcategories():
        subcategories_list = Subcategory.objects.all()
        if subcategories_list:
            return subcategories_list[0].id
        else:
            return None

    subcategory = models.ManyToManyField(
        Subcategory,
        verbose_name='Subcategorias',
    )

    def allAttributesOptions():
        atributes_options_list = AttributeOption.objects.all()
        if atributes_options_list:
            return atributes_options_list[0].id
        else:
            return None

    attribute_options = models.ManyToManyField(
        AttributeOption,
        verbose_name='Opções de Atributos',
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if str(self.slug) == '':
            self.slug = slugify("{} {}".format(self.name, self.code))
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']


class ProductPrice(models.Model):
    id_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    price = models.FloatField(
        verbose_name='Preço',
        null=False,
        blank=False,
        default=0.0
    )

    last_atualization = models.DateTimeField(
        verbose_name='Última atualização',
        null=False,
        blank=False,
        auto_now_add=True,
    )

    def __str__(self):
        return '{} - {}'.format(self.id_product, self.price)

    class Meta:
        verbose_name = 'Preço do Produto'
        verbose_name_plural = 'Preços de Produtos'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    p3_image_resize = models.ImageField(
        upload_to ='products_images/',
        null=False,
        blank=False,
        default='static/products/default.jpg',
        verbose_name='Imagem do produto.',
        help_text='Enviar arquivos .png ou .jpg.',
    )

    p3_image_size = models.CharField(
        max_length=100,
        default='1500x1000',
        editable=False,
    )

    alt = models.CharField(
        verbose_name='Nome da imagem',
        max_length=200,
        null=False,
        blank=False,
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
    )

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = 'Imagem do Produto'
        verbose_name_plural = 'Imagens do Produto'


class ProductStock(models.Model):
    id_product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

    quantity_produced = models.IntegerField(
        verbose_name='Quantidade produzida',
        null=False,
        blank=False,
        default=0
    )

    quantity_current = models.IntegerField(
        verbose_name='Quantidade atual',
        null=False,
        blank=False,
        default=0
    )

    def __str__(self):
        return '{} - {}'.format(self.id_product, self.quantity_produced)

    class Meta:
        verbose_name = 'Estoque de Produto'
        verbose_name_plural = 'Estoque de Produto'

# ------------------------------------------
# 04 - Grid de Categorias
# ------------------------------------------

class ProductCategoryGrid(CMSPlugin):

    main_category = models.ManyToManyField(Category, related_name="main_category_grid")

    second_category = models.ManyToManyField(Category, related_name="second_category_grid")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Grids de Categorias'
        verbose_name_plural = 'Grid de Categorias'

# ------------------------------------------
# 05 - Carrossel de Destaque de Produtos
# ------------------------------------------

# ------------------------------------------
# 06 - Grid de Produtos
# ------------------------------------------
