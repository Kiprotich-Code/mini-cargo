# Generated by Django 4.2.4 on 2024-08-27 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trackshipment',
            old_name='location',
            new_name='current_location',
        ),
    ]
