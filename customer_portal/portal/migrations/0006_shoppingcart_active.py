# Generated by Django 2.0.4 on 2018-04-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20180427_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]