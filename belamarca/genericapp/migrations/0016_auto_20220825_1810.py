# Generated by Django 3.0.14 on 2022-08-25 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericapp', '0015_auto_20220825_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericfooterplugin2',
            name='text_alt',
            field=models.CharField(default='Logo do Bela Marca', help_text='Digite o nome descritivo para a imagem.', max_length=100, verbose_name='Nome da imagem'),
        ),
    ]