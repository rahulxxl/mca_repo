# Generated by Django 3.0.5 on 2020-06-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200605_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='studio',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]