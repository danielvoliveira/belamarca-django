# Generated by Django 3.0.14 on 2022-08-25 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('genericapp', '0008_auto_20220617_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericfooterplugin2',
            name='g2_logo_image_resize',
            field=filer.fields.image.FilerImageField(help_text='Tamanho ideal 205x177.', on_delete=django.db.models.deletion.PROTECT, related_name='g2_logo_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem da logo.'),
        ),
        migrations.AlterField(
            model_name='genericfooterplugin2',
            name='g2_logo_image_size',
            field=models.CharField(default='205x177', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='genericheaderplugin1',
            name='g1_logo_image_resize',
            field=filer.fields.image.FilerImageField(help_text='Tamanho ideal 205x177.', on_delete=django.db.models.deletion.PROTECT, related_name='g1_logo_image_resize', to=settings.FILER_IMAGE_MODEL, verbose_name='Imagem da logo Ex.: Logo Branca.'),
        ),
        migrations.AlterField(
            model_name='genericheaderplugin1',
            name='g1_logo_image_size',
            field=models.CharField(default='205x177', editable=False, max_length=100),
        ),
    ]