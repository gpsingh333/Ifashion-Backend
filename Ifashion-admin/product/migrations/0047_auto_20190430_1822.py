# Generated by Django 2.1.5 on 2019-04-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0046_auto_20190430_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
