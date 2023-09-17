# Generated by Django 3.2.20 on 2023-09-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seoapp', '0003_auto_20230916_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seometatags',
            name='google_type',
            field=models.CharField(choices=[('Corporation', 'Corporação'), ('Organization', 'Organização'), ('product_list', 'Lista de Produtos'), ('product', 'Página de Produto')], default='Corporation', max_length=12, verbose_name='Modelo de Tags do Google a ser usado?'),
        ),
    ]
