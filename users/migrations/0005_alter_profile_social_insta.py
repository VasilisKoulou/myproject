# Generated by Django 4.2.2 on 2023-08-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_insta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]