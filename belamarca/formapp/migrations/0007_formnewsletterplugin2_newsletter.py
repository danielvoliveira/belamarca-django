# Generated by Django 3.0.14 on 2022-08-27 22:29

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('formapp', '0006_auto_20220827_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormNewsletterPlugin2',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='formapp_formnewsletterplugin2', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='Trabalhe Conosco', help_text='Título para o formulário.', max_length=100, verbose_name='Título')),
                ('subtitle', djangocms_text_ckeditor.fields.HTMLField(default='Preencha o formulário para receber um atendimento exclusivo da nossa equipe.', help_text='Subtítulo para o formulário.', max_length=500, verbose_name='Subtítulo')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('termos', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Cadastro da Newsletter',
                'verbose_name_plural': 'Cadastros das Newsletter',
            },
        ),
    ]
