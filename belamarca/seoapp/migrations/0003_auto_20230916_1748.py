# Generated by Django 3.2.20 on 2023-09-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seoapp', '0002_auto_20230916_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seometatags',
            options={'verbose_name': 'SEO Meta Tag', 'verbose_name_plural': 'SEO Meta Tags'},
        ),
        migrations.AddField(
            model_name='seometatags',
            name='google_type',
            field=models.CharField(choices=[('Corporation', 'Corporação'), ('Organization', 'Organização'), ('product_list', 'Lista de Produtos'), ('product', 'Página de Produto')], default='Corporation', editable=False, max_length=12, verbose_name='Modelo de Tags do Google a ser usado?'),
        ),
    ]