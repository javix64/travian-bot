# Generated by Django 3.2.3 on 2021-05-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travianAPI', '0004_auto_20210516_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='troops',
            name='attack',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='troops',
            name='carrying_capacity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='troops',
            name='crop_consumption',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='troops',
            name='defence_cavalry',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='troops',
            name='defence_infantry',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='troops',
            name='speed',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
