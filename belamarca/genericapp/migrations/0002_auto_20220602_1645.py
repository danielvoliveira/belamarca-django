# Generated by Django 3.0.14 on 2022-06-02 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('genericapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doubleimages',
            name='b2_first_image_resize',
        ),
        migrations.RemoveField(
            model_name='doubleimages',
            name='b2_second_image_resize',
        ),
        migrations.RemoveField(
            model_name='doubleimages',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='imagefullsizeplugin',
            name='b1_background_image_resize',
        ),
        migrations.RemoveField(
            model_name='imagefullsizeplugin',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='latestblogplugin',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='textsideimage',
            name='b2_side_image_resize',
        ),
        migrations.RemoveField(
            model_name='textsideimage',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='weekpostsplugin',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='youtubevideo',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='CenterText',
        ),
        migrations.DeleteModel(
            name='DoubleImages',
        ),
        migrations.DeleteModel(
            name='ImageFullSizePlugin',
        ),
        migrations.DeleteModel(
            name='LatestBlogPlugin',
        ),
        migrations.DeleteModel(
            name='TextSideImage',
        ),
        migrations.DeleteModel(
            name='WeekPostsPlugin',
        ),
        migrations.DeleteModel(
            name='YoutubeVideo',
        ),
    ]
