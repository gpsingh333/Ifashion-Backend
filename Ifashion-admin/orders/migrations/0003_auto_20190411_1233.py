# Generated by Django 2.1.5 on 2019-04-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190410_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeraddress',
            old_name='lag',
            new_name='log',
        ),
    ]