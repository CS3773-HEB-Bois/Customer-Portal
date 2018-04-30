# Generated by Django 2.0.4 on 2018-04-29 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_creditcardinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcardinformation',
            name='expiration_date',
        ),
        migrations.AddField(
            model_name='creditcardinformation',
            name='card_type',
            field=models.CharField(default='Visa', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creditcardinformation',
            name='month',
            field=models.CharField(default='12', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creditcardinformation',
            name='year',
            field=models.CharField(default='21', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentinformation',
            name='shopper',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, related_name='billing_options', to='portal.Shopper'),
            preserve_default=False,
        ),
    ]