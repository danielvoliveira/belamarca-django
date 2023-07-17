# Generated by Django 3.0.14 on 2022-06-08 21:48

from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('genericapp', '0004_auto_20220608_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericfooterplugin2',
            name='text_address',
            field=djangocms_text_ckeditor.fields.HTMLField(default='<p>Estrada Municipal Linha Ávila,<br>Rua Linha Carazal, 501<br>Gramado/RS - 95670-000</p>', help_text='Digite o endereço com rua, numero, bairro e cep.', max_length=200, verbose_name='Endereço completo'),
        ),
    ]
