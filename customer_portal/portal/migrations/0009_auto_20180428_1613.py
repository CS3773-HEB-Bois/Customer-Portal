# Generated by Django 2.0.4 on 2018-04-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20180428_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='discount',
            field=models.ManyToManyField(to='portal.Discount'),
        ),
    ]