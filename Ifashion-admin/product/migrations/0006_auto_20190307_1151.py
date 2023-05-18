# Generated by Django 2.1.5 on 2019-03-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer_stylist', '0007_stylistdesignersection'),
        ('product', '0005_auto_20190306_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='usersection',
        ),
        migrations.AddField(
            model_name='product',
            name='usersection',
            field=models.ManyToManyField(blank=True, to='designer_stylist.StylistDesignerSection'),
        ),
    ]
