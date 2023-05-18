# Generated by Django 2.1.5 on 2019-02-25 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userotherinfo_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotherinfo',
            name='rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
