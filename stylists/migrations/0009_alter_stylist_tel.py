# Generated by Django 3.2 on 2022-05-06 20:57

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('stylists', '0008_remove_stylist_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylist',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(default='Enter country code then telephone number', max_length=128, region=None),
        ),
    ]