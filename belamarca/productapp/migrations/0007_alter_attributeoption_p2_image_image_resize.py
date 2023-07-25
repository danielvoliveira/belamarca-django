# Generated by Django 3.2.20 on 2023-07-24 02:22

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('productapp', '0006_alter_attributeoption_p2_image_image_resize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributeoption',
            name='p2_image_image_resize',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Tamanho ideal 100x100.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2_image_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem do atributo.'),
        ),
    ]