# Generated by Django 2.1.5 on 2019-08-01 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0024_memberpaymenthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberpaymenthistory',
            name='payment_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
