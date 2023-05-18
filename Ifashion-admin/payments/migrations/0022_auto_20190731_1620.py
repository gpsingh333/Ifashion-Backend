# Generated by Django 2.1.5 on 2019-07-31 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0021_auto_20190731_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='cod_accepted_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cod_accepted_user', to=settings.AUTH_USER_MODEL),
        ),
    ]