# Generated by Django 4.2.4 on 2024-08-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_location_trackshipment_current_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='has_tracking',
            field=models.BooleanField(default=False),
        ),
    ]