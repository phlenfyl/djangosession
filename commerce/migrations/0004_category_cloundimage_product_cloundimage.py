# Generated by Django 4.2.7 on 2023-11-09 21:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_alter_category_image_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cloundImage',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='product',
            name='cloundImage',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Image'),
        ),
    ]
