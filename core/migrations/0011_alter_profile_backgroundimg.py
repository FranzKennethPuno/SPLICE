# Generated by Django 5.1.1 on 2024-10-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_profile_backgroundimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='backgroundimg',
            field=models.ImageField(upload_to='back_images'),
        ),
    ]
