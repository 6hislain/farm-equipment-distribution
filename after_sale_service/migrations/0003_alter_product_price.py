# Generated by Django 4.0.6 on 2022-08-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('after_sale_service', '0002_remove_product_link_remove_service_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
