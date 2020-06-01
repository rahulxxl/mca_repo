# Generated by Django 3.0.5 on 2020-05-28 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroom',
            name='room_type',
            field=models.CharField(blank=True, choices=[('delux', 'Delux'), ('premium', 'Premium'), ('delux_lounge', 'Delux Lounge')], max_length=50, null=True),
        ),
    ]