# Generated by Django 3.0.14 on 2022-06-17 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genericapp', '0007_auto_20220615_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genericfooterplugin2',
            name='url_faq',
        ),
        migrations.RemoveField(
            model_name='generictermsandconditionsplugin5',
            name='language',
        ),
        migrations.RemoveField(
            model_name='generictermsandconditionsplugin5',
            name='subtitle',
        ),
    ]