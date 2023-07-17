# Generated by Django 3.0.14 on 2022-08-29 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPlugin3',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bannerapp_bannerplugin3', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='', help_text='Insira o título.', max_length=150, verbose_name='Título')),
                ('subtitle', djangocms_text_ckeditor.fields.HTMLField(default='', max_length=1500, verbose_name='Descrição')),
                ('first_title', models.CharField(default='', help_text='Insira o título.', max_length=150, verbose_name='Primeiro título')),
                ('first_subtitle', djangocms_text_ckeditor.fields.HTMLField(default='', max_length=1500, verbose_name='Primeira descrição')),
                ('b3_first_image_size', models.CharField(default='630x508', editable=False, max_length=100)),
                ('first_text_alt', models.CharField(help_text='Digite o nome descritivo para a imagem.', max_length=100, verbose_name='Nome da imagem a esquerda')),
                ('second_title', models.CharField(default='', help_text='Insira o título.', max_length=150, verbose_name='Segundo título')),
                ('second_subtitle', djangocms_text_ckeditor.fields.HTMLField(default='', max_length=1500, verbose_name='Segunda descrição')),
                ('b3_second_image_size', models.CharField(default='630x508', editable=False, max_length=100)),
                ('second_text_alt', models.CharField(help_text='Digite o nome descritivo para a imagem.', max_length=100, verbose_name='Nome da imagem a esquerda')),
                ('third_title', models.CharField(default='', help_text='Insira o título.', max_length=150, verbose_name='Terceiro título')),
                ('third_subtitle', djangocms_text_ckeditor.fields.HTMLField(default='', max_length=1500, verbose_name='Terceira descrição')),
                ('b3_third_image_size', models.CharField(default='630x508', editable=False, max_length=100)),
                ('third_text_alt', models.CharField(help_text='Digite o nome descritivo para a imagem.', max_length=100, verbose_name='Nome da imagem a esquerda')),
                ('b3_first_image_resize', filer.fields.image.FilerImageField(blank=True, help_text='Tamanho ideal 630x508', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='b3_first_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem a esquerda')),
                ('b3_second_image_resize', filer.fields.image.FilerImageField(blank=True, help_text='Tamanho ideal 630x508', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='b3_second_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem a esquerda')),
                ('b3_third_image_resize', filer.fields.image.FilerImageField(blank=True, help_text='Tamanho ideal 630x508', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='b3_left_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem a esquerda')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BannerPlugin2',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bannerapp_bannerplugin2', serialize=False, to='cms.CMSPlugin')),
                ('b2_left_image_size', models.CharField(default='540x400', editable=False, max_length=100)),
                ('left_text_alt', models.CharField(help_text='Digite o nome descritivo para a imagem.', max_length=100, verbose_name='Nome da imagem a esquerda')),
                ('title', models.CharField(default='', help_text='Insira o título.', max_length=150, verbose_name='Título a direita')),
                ('subtitle', djangocms_text_ckeditor.fields.HTMLField(default='', max_length=1500, verbose_name='Descrição a direita')),
                ('b2_left_image_resize', filer.fields.image.FilerImageField(blank=True, help_text='Tamanho ideal 540x400', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='b2_left_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem a esquerda')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BannerPlugin1',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bannerapp_bannerplugin1', serialize=False, to='cms.CMSPlugin')),
                ('b1_background_image_size', models.CharField(default='1650x400', editable=False, max_length=100)),
                ('background_text_alt', models.CharField(help_text='Digite o nome descritivo para a imagem.', max_length=100, verbose_name='Nome da imagem a esquerda')),
                ('title', models.CharField(default='', help_text='Insira o título.', max_length=150, verbose_name='Título a direita')),
                ('subtitle', djangocms_text_ckeditor.fields.HTMLField(default='', max_length=1500, verbose_name='Descrição a direita')),
                ('b1_background_image_resize', filer.fields.image.FilerImageField(blank=True, help_text='Tamanho ideal 1650x400', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='b1_background_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem a esquerda')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
