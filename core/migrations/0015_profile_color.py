# Generated by Django 5.1.1 on 2024-10-07 14:05

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_profile_audio_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None),
        ),
    ]
