# Generated by Django 3.1.1 on 2020-11-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20201111_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zipcode',
            new_name='zip_code',
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]