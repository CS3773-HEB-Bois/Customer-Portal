# Generated by Django 2.0.4 on 2018-04-30 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_auto_20180429_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_information',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.BillingInformation'),
        ),
    ]
