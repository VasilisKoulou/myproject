# Generated by Django 4.2.2 on 2023-08-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='demo_link',
        ),
        migrations.RemoveField(
            model_name='product',
            name='source_link',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]