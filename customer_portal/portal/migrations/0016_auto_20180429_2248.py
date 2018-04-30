# Generated by Django 2.0.4 on 2018-04-30 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20180429_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverypreferences',
            name='deliverySpeed',
            field=models.CharField(default='standard', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_preferences',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.DeliveryPreferences'),
        ),
        migrations.AlterField(
            model_name='paymentinformation',
            name='shopper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_options', to='portal.Shopper'),
        ),
    ]
