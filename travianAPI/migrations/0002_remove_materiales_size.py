# Generated by Django 3.2.3 on 2021-05-16 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travianAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materiales',
            name='size',
        ),
    ]
