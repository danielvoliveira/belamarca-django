# Generated by Django 3.0.14 on 2022-08-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericapp', '0013_auto_20220825_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericfooterplugin2',
            name='g2_logo_image_size',
            field=models.CharField(default='205x177', editable=False, max_length=100),
        ),
    ]