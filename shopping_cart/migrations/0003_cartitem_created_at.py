# Generated by Django 4.0.8 on 2022-12-23 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
