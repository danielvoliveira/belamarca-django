# Generated by Django 3.0.14 on 2023-06-20 23:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome do atributo')),
                ('is_text', models.BooleanField(default=False)),
                ('is_image', models.BooleanField(default=False)),
                ('is_color', models.BooleanField(default=False)),
                ('disp', models.CharField(choices=[('disponivel', 'Disponível'), ('indisponivel', 'Indisponível')], default='disponivel', max_length=12, verbose_name='Disponibilidade')),
            ],
            options={
                'verbose_name': 'Atributo',
                'verbose_name_plural': 'Atributos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AttributeOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120, verbose_name='Nome do atributo')),
                ('text', models.CharField(blank=True, max_length=120, null=True, verbose_name='Texto do atributo')),
                ('p2_image_image_size', models.CharField(default='100x100', editable=False, max_length=100)),
                ('color', models.CharField(blank=True, max_length=7, null=True, verbose_name='Hexadecimal da cor')),
                ('disp', models.CharField(choices=[('disponivel', 'Disponível'), ('indisponivel', 'Indisponível')], default='disponivel', max_length=12, verbose_name='Disponibilidade')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productapp.Attribute')),
                ('p2_image_image_resize', filer.fields.image.FilerImageField(blank=True, help_text='Tamanho ideal 100x100.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='p2_image_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem do atributo.')),
            ],
            options={
                'verbose_name': 'Opção de Atributo',
                'verbose_name_plural': 'Opções de Atributos',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome da categoria')),
                ('disp', models.CharField(choices=[('disponivel', 'Disponível'), ('indisponivel', 'Indisponível')], default='disponivel', max_length=12, verbose_name='Disponibilidade')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='Código do produto')),
                ('name', models.CharField(max_length=150, verbose_name='Nome do produto')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', help_text='Digite a descrições do produto', max_length=1000, null=True, verbose_name='Descrição')),
                ('datasheet', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', help_text='Digite as específicações do produto', max_length=1000, null=True, verbose_name='Ficha Técnica')),
                ('slug', models.SlugField(blank=True, default='', max_length=300, unique=True, verbose_name='Slug do produto')),
                ('disp', models.CharField(choices=[('disponivel', 'Disponível'), ('indisponivel', 'Indisponível')], default='disponivel', max_length=12, verbose_name='Disponibilidade')),
                ('attribute_options', models.ManyToManyField(to='productapp.AttributeOption', verbose_name='Opções de Atributos')),
                ('category', models.ManyToManyField(to='productapp.Category', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome da subcategoria')),
                ('disp', models.CharField(choices=[('disponivel', 'Disponível'), ('indisponivel', 'Indisponível')], default='disponivel', max_length=12, verbose_name='Disponibilidade')),
            ],
            options={
                'verbose_name': 'Subcategoria',
                'verbose_name_plural': 'Subcategorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_produced', models.IntegerField(default=0, verbose_name='Quantidade produzida')),
                ('quantity_current', models.IntegerField(default=0, verbose_name='Quantidade atual')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productapp.Product')),
            ],
            options={
                'verbose_name': 'Estoque de Produto',
                'verbose_name_plural': 'Estoque de Produto',
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0, verbose_name='Preço')),
                ('last_atualization', models.DateTimeField(default=datetime.datetime.now, verbose_name='Última atualização')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productapp.Product')),
            ],
            options={
                'verbose_name': 'Preço do Produto',
                'verbose_name_plural': 'Preços de Produtos',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p3_image_resize', models.ImageField(default='static/products/default.jpg', help_text='Enviar arquivos .png ou .jpg.', upload_to='products_images/', verbose_name='Imagem do produto.')),
                ('p3_image_size', models.CharField(default='1500x1000', editable=False, max_length=100)),
                ('alt', models.CharField(max_length=200, verbose_name='Nome da imagem')),
                ('disp', models.CharField(choices=[('disponivel', 'Disponível'), ('indisponivel', 'Indisponível')], default='disponivel', max_length=12, verbose_name='Disponibilidade')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productapp.Product')),
            ],
            options={
                'verbose_name': 'Imagem do Produto',
                'verbose_name_plural': 'Imagens do Produto',
            },
        ),
        migrations.CreateModel(
            name='ProductCategoryGrid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='productapp_productcategorygrid', serialize=False, to='cms.CMSPlugin')),
                ('main_category', models.ManyToManyField(related_name='main_category_grid', to='productapp.Category')),
                ('second_category', models.ManyToManyField(related_name='second_category_grid', to='productapp.Category')),
            ],
            options={
                'verbose_name': 'Grids de Categorias',
                'verbose_name_plural': 'Grid de Categorias',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ManyToManyField(to='productapp.Subcategory', verbose_name='Subcategorias'),
        ),
    ]