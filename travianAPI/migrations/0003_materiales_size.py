# Generated by Django 3.2.3 on 2021-05-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travianAPI', '0002_remove_materiales_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiales',
            name='size',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
