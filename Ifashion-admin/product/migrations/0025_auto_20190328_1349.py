# Generated by Django 2.1.5 on 2019-03-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20190328_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponcode',
            name='valid_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='valid_to',
            field=models.DateField(),
        ),
    ]
