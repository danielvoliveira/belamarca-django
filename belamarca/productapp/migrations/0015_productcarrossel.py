# Generated by Django 3.2.20 on 2023-08-01 21:13

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20230723_2308'),
        ('productapp', '0014_alter_attributeoption_p2_image_image_resize'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCarrossel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='productapp_productcarrossel', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome do produto')),
                ('subtitle', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', help_text='Digite a descrições do produto', max_length=1000, null=True, verbose_name='Descrição')),
                ('products', models.ManyToManyField(related_name='products_to_carrossel', to='productapp.Product')),
            ],
            options={
                'verbose_name': 'Carrosel de Produtos',
                'verbose_name_plural': 'Carrossíes de Produtos',
            },
            bases=('cms.cmsplugin',),
        ),
    ]