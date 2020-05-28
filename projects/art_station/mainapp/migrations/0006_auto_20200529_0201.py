# Generated by Django 3.0.5 on 2020-05-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200529_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='imageinfostudio',
            name='image_store',
        ),
        migrations.RemoveField(
            model_name='imageinfostudio',
            name='owner',
        ),
        migrations.DeleteModel(
            name='ImageMainStore',
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
        migrations.RemoveField(
            model_name='location',
            name='state',
        ),
        migrations.RemoveField(
            model_name='location',
            name='studio',
        ),
        migrations.RemoveField(
            model_name='state',
            name='country',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='subscription',
        ),
        migrations.RemoveField(
            model_name='studio',
            name='subscription',
        ),
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='ImageInfoStudio',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]