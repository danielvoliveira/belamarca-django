# Generated by Django 3.0.14 on 2022-08-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericapp', '0011_auto_20220825_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericheaderplugin1',
            name='g1_logo_image_size',
            field=models.CharField(default='205x177', editable=False, max_length=100),
        ),
    ]
