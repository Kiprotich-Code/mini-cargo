# Generated by Django 4.2.4 on 2024-09-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_name', models.CharField(max_length=100)),
                ('receiver_email_address', models.EmailField(max_length=254)),
                ('receiver_location', models.CharField(max_length=55)),
                ('receiver_address', models.CharField(max_length=250)),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email_address', models.EmailField(max_length=254)),
                ('sender_location', models.CharField(max_length=55)),
                ('sender_address', models.CharField(max_length=250)),
                ('sender_phone_no', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('qnty', models.CharField(max_length=55)),
                ('shipped_from', models.CharField(max_length=100)),
                ('shipped_to', models.CharField(max_length=100)),
                ('expected_shipping_date', models.DateField()),
                ('expected_arrival_date', models.DateField()),
                ('estimated_budget', models.IntegerField()),
                ('additional_info', models.TextField()),
            ],
        ),
    ]
