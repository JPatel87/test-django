# Generated by Django 3.2 on 2022-05-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20220530_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='time',
            field=models.CharField(default='', max_length=5),
        ),
    ]