# Generated by Django 3.2 on 2022-05-06 20:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('stylists', '0006_alter_stylist_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylist',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(default='SOME STRING', max_length=128, region=None),
        ),
    ]
