# Generated by Django 3.2.20 on 2023-07-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0012_alter_attributeoption_p2_image_image_resize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributeoption',
            name='p2_image_image_resize',
            field=models.ImageField(blank=True, default='products_images/default.jpg', help_text='Enviar arquivos .png ou .jpg. Tamanho ideal 100x100.', null=True, upload_to='products_images/prints/', verbose_name='Imagem do atributo.'),
        ),
    ]
